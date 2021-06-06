from django import forms

class NameForm(forms.Form):
    name=forms.CharField()

class AgeForm(forms.Form):
    age=forms.CharField()

class GfForm(forms.Form):
    GF=forms.CharField()
