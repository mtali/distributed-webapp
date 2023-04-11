from rest_framework import serializers

from sales.models import Membership


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'name', 'price', 'duration_in_days', 'created_at', 'updated_at']
