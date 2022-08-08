from django.urls import path
from course import views

urlpatterns = [
     path('course/', views.course, name='course'),
     path('coursehome<str:slug>', views.coursehome, name='coursehome'),
     path('buycourse', views.buycourse, name='buycourse'),
     path('search', views.search, name='search')
   
    
]