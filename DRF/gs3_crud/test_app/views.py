from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def student_get(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        print(parsed_data)   # {'id' : id }
        id=parsed_data.get('id',None)
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")
        resp={'msg':" id is None "}
        json_resp=json.dumps(resp)
        return HttpResponse(json_resp,content_type="application/json")


@csrf_exempt
def student_post(request):
    """
    json_data   ---> python_data :-
                json_data ===>stream ===> serializer ===> parsed_data==>python_data=serializer.data
    python_data ---->  j
                 python_data ===>  json_data=render(python_data)

    """
    if request.method=="POST":
        json_data=request.body         #data from 3rd party application
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        print("parsed data ",parsed_data)
        serializer=StudentSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':"Data saved successfully"}
            #serializer_msg=StudentSerializer(msg)
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        msg={'msg':"Data is Invalid"}
        #serializer_msg=StudentSerializer(msg)
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type="application/json")


@csrf_exempt
def student_update(request):
    if request.method=='PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream) #python_data
        id=parsed_data.get('id')
        std=Student.objects.get(id=id)
        print(std.name)
        print(std.id)
        print(std.marks)
        serializer = StudentSerializer(std,data=parsed_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Data is Updated successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        #msg={'msg':"Data is not proper "}
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def student_delete(request):
    if request.method=="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id=python_data.get('id')
        std=Student.objects.get(id=id)
        std.delete()
        msg={'msg':'student data deleted successfully'}
        return JsonResponse(msg,safe=False)






