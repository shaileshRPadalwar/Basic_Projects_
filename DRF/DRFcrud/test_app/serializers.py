from rest_framework import serializers

#create serializers

class EmployeeSerializer(serializers.Serializer):
    ename=serializers.CharField()
    enum=serializers.IntegerField()
    esal=serializers.FloatField()

