from django.shortcuts import render
from course.models import Course, CourseLesson, Video




# Create your views here.
def course(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'course/course.html',context)


def coursehome(request,slug):
    course = Course.objects.get(sno =slug)
    course_lessons = CourseLesson.objects.filter(lesson_model = course)
    
    videos = Video.objects.filter(video_course  = course)
    print(videos)
    
    
    context  ={'course': course, 'course_lessons' : course_lessons , 'videos': videos }
   
   
    return render(request, 'course/coursehome.html', context)