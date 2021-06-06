from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')


@login_required
def java(request):
    return render(request,'testapp/java.html')

def python(request):
    return render(request,'testapp/python.html')

def aptitude(request):
    return render(request,'testapp/aptitude.html')

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()     #user object or table name
        user.set_password(user.password) #To convert password in encripted form
        user.save() #save data in database
    return render(request,'testapp/signup.html',{'form':form})
