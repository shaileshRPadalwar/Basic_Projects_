from django.urls import path
from .views import *


urlpatterns=[
    path('name/',name),
    path('age/',age),
    path('gf/',gf),
    path('result/',result),
]