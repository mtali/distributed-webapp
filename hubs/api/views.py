from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from hubs.api.serializer import DeviceInfoSerializer
from hubs.models import Hub
from webapp.permissions import DeviceIDHeaderPermission


class DeviceInfoApiView(APIView):
    permission_classes = [DeviceIDHeaderPermission]

    def get(self, request):
        device_id = request.headers.get('X-DEVICE-ID')
        hub = Hub.objects.filter(device_id=device_id).first()
        serializer = DeviceInfoSerializer(hub)
        return Response(serializer.data, status=status.HTTP_200_OK)
