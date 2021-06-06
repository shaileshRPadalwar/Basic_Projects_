from django.urls import path
from testapp import views

urlpatterns=[
    path('registration/',views.registration),
]
