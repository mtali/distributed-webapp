from rest_framework import serializers

from packs.models import Pack


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = [
            'pack_id',
            'pack_status',
            'current_customer_id',
            'is_active',
            'created_at',
            'updated_at'
        ]
