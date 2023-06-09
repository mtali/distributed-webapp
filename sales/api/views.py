from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from sales.api.serializers import MembershipSerializer
from sales.models import Membership
from webapp.permissions import DeviceIDHeaderPermission


class MembershipListApiView(APIView):
    permission_classes = [DeviceIDHeaderPermission]

    def get(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
