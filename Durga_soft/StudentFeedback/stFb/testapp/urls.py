from django.urls import path
from .views import feedback ,registration

urlpatterns=[

    path('feedback/',feedback,name='feedback'),
    path('signup/',registration),

]