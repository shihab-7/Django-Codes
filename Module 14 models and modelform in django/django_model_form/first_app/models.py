from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.IntegerField(primary_key= True)
    address = models.TextField()
    father_name = models.TextField(default='karim')

    # new field create na korle migrate command run koarar lagbe na , function create korle automatically oita adjust hoye jabe

# ei function ta admin panel a object name hishebe na show kore direct define kora name gulo show korbe
    def __str__(self):
         return f'Roll : {self.roll} - {self.name}'