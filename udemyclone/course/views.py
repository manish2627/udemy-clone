from django.shortcuts import render
from course.models import Course, CourseLesson




# Create your views here.
def coursehome(request,slug):
    course = Course.objects.get(sno =slug)
    course_lessons = CourseLesson.objects.filter(lesson_model = course)
    context  ={'course': course, 'course_lessons' : course_lessons}
    print(course_lessons)
    return render(request, 'course/coursehome.html', context)