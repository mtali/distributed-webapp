from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRootView(APIView):
    def get(self, request):
        data = {
            'memberships': reverse('memberships-list'),
        }
        return Response(data)
