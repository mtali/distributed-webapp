from rest_framework import serializers


class DeviceInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    device_id = serializers.CharField()
    country = serializers.CharField()
    region = serializers.CharField()

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def create(self, validated_data):
        raise NotImplementedError()
