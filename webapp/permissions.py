from rest_framework import permissions

from hubs.models import Hub


class DeviceIDHeaderPermission(permissions.BasePermission):
    message = 'Device ID not found'

    def has_permission(self, request, view):
        device_id = request.headers.get('X-DEVICE-ID')
        hub = Hub.objects.filter(device_id=device_id).first()
        if not hub:
            return False
        return True
