from django.contrib import admin
from course.models import Course,CourseLesson,Video,Purchasecourse


# Register your models here.
admin.site.register(Course)
admin.site.register(CourseLesson)
admin.site.register(Video)
admin.site.register(Purchasecourse)