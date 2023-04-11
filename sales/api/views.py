from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from sales.api.serializers import MembershipSerializer
from sales.models import Membership


class MembershipListApiView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        device_id = request.headers['X-DEVICE-ID']
        if not device_id:
            return Response({'error': 'Device ID not found'}, status=400)

        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
