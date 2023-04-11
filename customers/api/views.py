from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from customers.api.serializers import CustomerSerializer
from customers.models import Customer
from webapp.permissions import DeviceIDHeaderPermission


class CustomersListApiView(APIView):
    permission_classes = [DeviceIDHeaderPermission]

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
