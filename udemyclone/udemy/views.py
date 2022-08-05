import math
from django.shortcuts import render,HttpResponse
from course.models import Course
from math import ceil 

# Create your views here.
def home(request):
    courses = Course.objects.all()
    n= len(courses)
    nSlides= n//4 + ceil((n/4) + (n//4))
    context = {"courses": courses, 'range':range(0,nSlides)}
    return render(request, 'home/home.html', context)