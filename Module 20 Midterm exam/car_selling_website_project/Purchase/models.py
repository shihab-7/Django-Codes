from django.db import models
from Cars.models import Car
from django.contrib.auth.models import User

# Create your models here.
class UserPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    car_quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits= 20, decimal_places=2, default=0, null=True,blank=True)

    def __str__(self):
        return f"{self.user.first_name} bought {self.car.name}"