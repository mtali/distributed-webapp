from rest_framework import serializers

from customers.models import Customer


class UserWebhookSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    birth_date = serializers.IntegerField()
    phone_number = serializers.CharField(max_length=255)
    guarantor_first_name = serializers.CharField(max_length=255)
    guarantor_last_name = serializers.CharField(max_length=255)
    guarantor_phone = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def create(self, validated_data):
        return Customer(
            {
                ''
            }
        )
