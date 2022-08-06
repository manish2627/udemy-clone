from django.contrib import admin
from course.models import Course,CourseLesson,Video


# Register your models here.
admin.site.register(Course)
admin.site.register(CourseLesson)
admin.site.register(Video)