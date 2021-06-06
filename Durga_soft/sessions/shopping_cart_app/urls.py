from django.urls import path
from shopping_cart_app import views


urlpatterns=[

    path('additem/',views.additem),
    #path('home/'),
    #path(''),
]


