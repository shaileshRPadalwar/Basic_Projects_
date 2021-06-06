from django import forms
from .models import StudentRegistration

class StudentRegistrationForm(forms.ModelForm):
    #fields with validations

    class Meta:
        model=StudentRegistration
        fields='__all__'