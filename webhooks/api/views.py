import uuid
from datetime import datetime, timezone

from django.utils import timezone as d_timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.models import Customer
from hubs.models import Hub
from packs.models import Pack
from sales.models import Transaction
from webapp.permissions import DeviceIDHeaderPermission
from webhooks.models import Webhook


class WebhookApiView(APIView):
    permission_classes = [DeviceIDHeaderPermission]

    def post(self, request):
        device_id = request.headers.get('X-DEVICE-ID')
        hub = Hub.objects.filter(device_id=device_id).first()
        root_data = request.data
        webhook_type = root_data.get('type')
        aware_timestamp = datetime.fromtimestamp(int(root_data.get('timestamp')), tz=timezone.utc)
        webhook, created = Webhook.objects.update_or_create(
            id=root_data.get('uid'),
            defaults={
                'id': root_data.get('uid'),
                'type': root_data.get('type'),
                'payload': root_data,
                'timestamp': aware_timestamp,
            }
        )

        if webhook.processed:
            return Response({"status": "ok"})

        data = root_data.get('data')
        if webhook_type == 'NewUser' or webhook_type == 'UpdateUser':
            Customer.objects.update_or_create(
                id=data.get('id'),
                defaults={
                    'first_name': data.get('first_name'),
                    'last_name': data.get('last_name'),
                    'phone': data.get('phone_number'),
                    'gender': data.get('gender'),
                    'address': data.get('address'),
                    'guarantor_first_name': data.get('guarantor_first_name'),
                    'guarantor_last_name': data.get('guarantor_last_name'),
                    'guarantor_phone': data.get('guarantor_phone'),
                    'hub': hub,
                }
            )
            webhook.processed = True
            webhook.save()
            return Response({"status": "ok"})
        elif webhook_type == 'MembershipSale':
            customer = Customer.objects.get(id=data.get('customer_id'))
            Transaction.objects.get_or_create(
                id=webhook.id,
                customer=customer,
                amount=data.get('payment_amount'),
                pack_in=None,
                pack_out=None,
                type='Membership',
                duration_in_days=data.get('duration')
            )
            customer.update_membership(data.get('duration'))
            webhook.processed = True
            webhook.save()
            return Response({"status": "ok"})

        elif webhook_type == 'SwapSale':
            customer = Customer.objects.get(id=data.get('customer_id'))

            if data.get('pack_in'):
                pack_in, _ = Pack.objects.update_or_create(
                    pack_id=data.get('pack_in'),
                    defaults={
                        'pack_id': data.get('pack_in'),
                        'hub': hub,
                        'pack_status': 'AtHubUncharged',
                        'current_customer': None,
                        'is_active': True,
                    }
                )
            else:
                pack_in = None

            if data.get('pack_out'):
                pack_out, _ = Pack.objects.update_or_create(
                    pack_id=data.get('pack_out'),
                    defaults={
                        'pack_id': data.get('pack_out'),
                        'hub': hub,
                        'pack_status': 'SignedOut',
                        'current_customer': customer,
                        'is_active': True,
                    }
                )
            else:
                pack_out = None

            Transaction.objects.get_or_create(
                id=webhook.id,
                customer=customer,
                amount=0,
                pack_in=pack_in,
                pack_out=pack_out,
                type='Swap',
                duration_in_days=None
            )
            webhook.processed = True
            webhook.save()
            return Response({"status": "ok"})


class HubApiView(APIView):

    def get(self, request, pack_id, status):
        data = {
            "pack_id": pack_id,
            "status": status,
        }
        Webhook.objects.create(
            id=str(uuid.uuid4()),
            type="PackUpdate",
            payload={"data": request.data},
            timestamp=d_timezone.now(),
            processed=False,
        )
        return Response(data="success")
