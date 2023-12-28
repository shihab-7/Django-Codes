from django.db import models
from CarBrands.models import Brands

# Create your models here.
class Car(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'cars/', blank=True, null=True)
    price = models.DecimalField(max_digits=10 , decimal_places= 2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Car name : {self.name}'
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.name}"