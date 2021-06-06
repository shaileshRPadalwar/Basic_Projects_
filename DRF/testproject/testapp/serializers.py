from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField()
    roll=serializers.IntegerField()
    marks=serializers.FloatField()
    #To create data in the database
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.marks = validated_data.get('marks',instance.marks)
        instance.save()
        return validated_data









