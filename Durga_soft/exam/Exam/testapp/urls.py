from django.urls import path
from testapp import views
urlpatterns=[

    path('',views.home),
    path('java/',views.java),
    path('python/',views.python),
    path('aptitude/',views.aptitude),
    path('signup/',views.signup),

]


