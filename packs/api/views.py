from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from hubs.models import Hub
from packs.api.serializers import PackSerializer
from packs.models import Pack
from webapp.permissions import DeviceIDHeaderPermission


class PacksListApiView(APIView):
    permission_classes = [DeviceIDHeaderPermission]

    def get(self, request):
        device_id = request.headers.get('X-DEVICE-ID')
        hub = Hub.objects.filter(device_id=device_id).first()
        packs = Pack.objects.filter(hub=hub, is_active=True)
        serializer = PackSerializer(packs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
