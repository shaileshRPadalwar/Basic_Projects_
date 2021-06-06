from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.
class TestApiView(APIView):
    def get(self,request,format=None):
        colors=['RED','BLUE','GREEN','YELLOW','INDIGO']
        return Response({'msg':'Welcome to colorful Year','colors':colors})


#Learing serialization

def employee(request,id):
    emp=Employee.objects.get(id=id)
    #print(type(emp))
    eserializer=EmployeeSerializer(emp)
    # print(type(eserializer))
    # print("eserializer : ",eserializer)
    # print("eserializer.data : ", eserializer.data)
    ##json_data=JSONRenderer().render(eserializer.data)
    #print(type(json_data))
    ##return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(eserializer.data)

def employees(request):
    emps=Employee.objects.all()
    eser=EmployeeSerializer(emps,many=True)
    print(eser.data) #python native data type
    json_data=JSONRenderer().render(eser.data)
    return HttpResponse(json_data,content_type="application/json")

#deserialization ==> converting python native data type to complex data like queryset

#json_data--->python data --> stream-->complex

import io
from rest_framework.parsers import JSONParser
def employees_deser(request):
    emps=Employee.objects.all()
    eser=EmployeeSerializer(emps,many=True)
    python_data=eser.data
    print(type(python_data))
    json_data=JSONRenderer().render(python_data)
    stream=io.BytesIO(json_data)
    data=JSONParser().parse(stream)
    serializer=EmployeeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    print("deserialization : ",type(data))
    return HttpResponse(data)







