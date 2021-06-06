from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CrudSerializer

# Create your views here.

class Crud_Api(APIView):
    def get(self,request,*args,**kwargs):
        msg={'msg':"This message is from get method"}
        return Response(msg['msg'])
    """
    In post request partner application sends data in the form of json.
    To convert json data to python data we need serializer.
    
    """
    def post(self,request,*args,**kwargs):
        json_data = request.data
        serializer = CrudSerializer(data=json_data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg={'msg':"Data saved successfully"}
            return Response(msg)
        else:
            msg={'msg':"Data not saved Due to Validation Error"}
            return Response(msg)
    def delete(self,request,pk=None):
        msg={'msg':"This response is from delete method"}
        return Response(msg)
    def put(self,request,pk=None):
        msg={'msg':"This response is from put method"}
        return Response(msg)
    def patch(self,request,pk=None):
        msg={'msg':"This response is from patch method"}
        return Response(msg)
