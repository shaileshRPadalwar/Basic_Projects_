from django.shortcuts import render,redirect
from testapp import forms
from .models import Movie

# Create your views here.
def add_movie_view(request):
    form=forms.MovieForms()
    if request.method=='POST':
        form=forms.MovieForms(request.POST)
        if form.is_valid():
            form.save()
        return movie_list_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})

def movie_list_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movies_list':movies_list})


def home(request):

    return render(request,'testapp/home.html')





