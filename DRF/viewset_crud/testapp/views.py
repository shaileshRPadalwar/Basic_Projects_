from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
# Create your views here.


class Crud_Viewset(ViewSet):
    def retrieve(self,request):
        msg={'msg':"Response is from retrieve method of Viewset"}
        return Response(msg)




