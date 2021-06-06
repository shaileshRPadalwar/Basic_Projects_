from django.shortcuts import render
from webapp import forms
# Create your views here.
'''
Take information of student name and marks
'''
def student(request):
    form=forms.StudentForm() #object creation to pass to template
    return render(request,'base.html',{'form':form})


