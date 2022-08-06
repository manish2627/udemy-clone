from django.db import models

# Create your models here.
class Course(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    price = models.FloatField( )
    desc = models.CharField(max_length=50, default="")
    content = models.TextField(default="")

    image = models.ImageField()

    def __str__(self) :
        return self.title

class CourseLesson(models.Model):
    sno = models.AutoField(primary_key= True)
    lesson_name = models.CharField(max_length=50)
    lesson_model = models.ForeignKey(Course, on_delete=models.CASCADE)
    class Meta:
        db_table='lesson_name'
    def __str__(self):
        return self.lesson_name


class Video(models.Model):
    sno = models.AutoField(primary_key=True)
    video_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_lesson = models.ForeignKey(CourseLesson, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=20)
    video_link = models.CharField(max_length=100)
    video_desc = models.TextField(default="")

    def __str__(self) :
        return self.video_name

class Purchasedcourse(models.Model):
    cust_id=models.IntegerField()
    purchase_id=models.IntegerField()
    price=models.IntegerField()
    
    
