from django.urls import path
from .views import *
urlpatterns=[

    path('addmovie/',add_movie_view,name='addmovie'),
    path('listmovie/',movie_list_view),
    path('home/',home),
]