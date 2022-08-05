from django.urls import path
from udemy import views

urlpatterns = [
     path('', views.home, name='home')
   
    
]