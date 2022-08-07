from django.urls import path
from course import views

urlpatterns = [
     path('', views.course, name='course'),
     path('coursehome<str:slug>', views.coursehome, name='coursehome')
   
    
]