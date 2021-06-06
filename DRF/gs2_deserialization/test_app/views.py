from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from .serializers import StudentSerialiazer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        print("in post method")
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        serializer=StudentSerialiazer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Student Data created successfully"}
            json_data=JSONParser().parse(res)
            return HttpResponse(json_data,content_type="application/json")
        print("out of post method ")
        json_data=JSONParser().parse(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")



