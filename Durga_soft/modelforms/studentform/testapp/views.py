from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def registration(request):
    form=StudentRegistrationForm() #Empty form for user
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST)#TO capture all data from user
        if form.is_valid():
            print("Form is validated")
            print(form.cleaned_data)
            form.save()
        return render(request,'testapp/thankyou.html',{'form':form})

    return render(request,'testapp/studentform.html',{'form':form})
