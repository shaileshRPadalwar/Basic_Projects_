from django.shortcuts import render
from .forms import FeedbackForm,StudentRegistration

# Create your views here.
def feedback(request):
    form=FeedbackForm()
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        ##print("without validations :",form.cleaned_data)
        #without validations form will not submit
        if form.is_valid():
            print("validations full-filled")
            print(form.cleaned_data)
            print("Name :",form.cleaned_data['name'])
            print("Roll No. ",form.cleaned_data['rollno'])
            print('Email :',form.cleaned_data['email'])
            print("Password",form.cleaned_data['password'])
            print("re-password :",form.cleaned_data['rpassword'])
            print("Feedback :",form.cleaned_data['feedback'])
            return render(request,'testapp/thankyou.html')
    return render(request,'testapp/base.html',{'form':form})

#Student registration form

def registration(request):
    form=StudentRegistration()
    if request.method=='POST':
        form=StudentRegistration(request.POST) #object creation to capture all the data from the user
        if form.is_valid():
            print(form.cleaned_data)
    return render(request,'testapp/signup.html',{'form':form})



