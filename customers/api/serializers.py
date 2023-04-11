from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'gender',
            'address',
            'guarantor_first_name',
            'guarantor_last_name',
            'guarantor_phone',
            'membership_expiry_date',
            'created_at',
            'updated_at',
        ]
