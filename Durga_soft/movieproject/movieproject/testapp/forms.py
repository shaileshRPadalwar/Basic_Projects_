from django import forms
from .models import Movie

class MovieForms(forms.ModelForm):

    # write validations here
    rdate=forms.DateField(label='Released Date\n(mm/dd/yyyy)')
    class Meta:
        model=Movie
        fields='__all__'

