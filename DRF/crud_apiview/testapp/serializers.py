from rest_framework import serializers


class CrudSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)

