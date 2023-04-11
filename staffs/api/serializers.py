from rest_framework import serializers

from customers.api.serializers import CustomerSerializer
from staffs.models import Staff


class StaffSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Staff
        fields = "__all__"
