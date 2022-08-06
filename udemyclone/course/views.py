from django.shortcuts import render
from course.models import Course



# Create your views here.
def coursehome(request,slug):
    course = Course.objects.get(sno =slug)
    context  ={'course': course}
    print(course.title)
    return render(request, 'course/coursehome.html', context)