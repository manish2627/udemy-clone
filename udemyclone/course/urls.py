from django.urls import path
from course import views

urlpatterns = [
     # path('', views.coursehome, name='cours')
     path('coursehome<str:slug>', views.coursehome, name='coursehome-detail')
   
    
]