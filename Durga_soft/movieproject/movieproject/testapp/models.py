'''
Steps : models.py,admin.py,forms.py,views.py,html,urls

'''

from django.db import models
from datetime import datetime,date
# Create your models here.
class Movie(models.Model):
    rdate=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()

