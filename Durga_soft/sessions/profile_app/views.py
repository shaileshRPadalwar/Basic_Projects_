from django.shortcuts import render
from .forms import NameForm,AgeForm,GfForm

# Create your views here.

def name(request):
    form=NameForm()
    return render(request,'profile/name.html',{'form':form})

def age(request):
    name=request.POST['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'profile/age.html',{'form':form,'name':name})

def gf(request):
    age=request.GET['age']
    request.session['age']=age
    form=GfForm()
    return render(request,'profile/gf.html',{'form':form})

def result(request):
    gf=request.GET['GF']
    name=request.session['name']
    age=request.session['age']
    request.session['gf']=gf
    return render(request,'profile/result.html',{'name':name,'age':age,'gf':gf})






