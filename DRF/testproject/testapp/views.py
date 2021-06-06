from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def get_student(request):
    json_data=request.body
    stream=io.BytesIO(json_data)
    python_data=JSONParser().parse(stream)
    id=python_data.get('id',None)
    if id is not None:
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu)
        #python_data=
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")


@csrf_exempt
def post_student(request):
    #if request.method=="POST":
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        msg = {'msg': " Data saved successfully "}
        return JsonResponse(msg['msg'], safe=False)
    return JsonResponse(serializer.errors, safe=False)

@csrf_exempt
def delete_student(request):
    json_data=request.body
    stream=io.BytesIO(json_data)
    python_data=JSONParser().parse(stream)
    id=python_data.get('id',None)
    if id is not None:
        stu=Student.objects.get(id=id)
        stu.delete()
        msg={'msg':"data deleted successfully ",'id':id}
        return JsonResponse(msg['msg'],safe=False)
    msg={'msg':"something is wrong"}
    return JsonResponse(msg['msg'],safe=False)


@csrf_exempt
def update_student(request):
    json_data=request.body
    stream=io.BytesIO(json_data)
    python_data=JSONParser().parse(stream)
    id=python_data.get('id',None)
    if id is not None:
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(instance=stu,partial=True,data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':" Data updated successfully "}
            return JsonResponse(msg,safe=False)
        msg={'msg':" Data not updated successfully "}
        return JsonResponse(msg,safe=False)
    msg={'msg':" id is incorrect "}
    return JsonResponse(msg,safe=False)





