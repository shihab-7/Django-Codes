from django.db import models

# Create your models here.

class Brands(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100 , null=True, blank=True , unique=True)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)    

    def __str__(self):
        return self.name