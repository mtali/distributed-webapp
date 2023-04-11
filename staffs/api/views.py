from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from hubs.models import Hub
from staffs.api.serializers import StaffSerializer
from staffs.models import Staff
from webapp.permissions import DeviceIDHeaderPermission


class StaffsListApiView(APIView):
    permission_classes = [DeviceIDHeaderPermission]

    def get(self, request):
        device_id = request.headers.get('X-DEVICE-ID')
        hub = Hub.objects.filter(device_id=device_id).first()
        staffs = Staff.objects.filter(customer__hub=hub, is_active=True)
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
