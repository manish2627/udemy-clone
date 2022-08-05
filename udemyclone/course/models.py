from django.db import models

# Create your models here.
class Course(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="")
    price = models.FloatField( )
    desc = models.CharField(max_length=50, default="")
    image = models.ImageField()

    def __str__(self) :
        return self.title
