from rest_framework import serializers
from .models import Student

class StudentSerialiazer(serializers.Serializer):
    name=serializers.CharField()
    roll=serializers.IntegerField()
    marks=serializers.FloatField()
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

