from django.db.models.base import Model as Model
from django.shortcuts import render,redirect
from .models import UserPurchase
from Cars.models import Car
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def UserPurchaseView(request, pk=None):
    if request.user.is_authenticated:
        b_user = request.user
        b_car = Car.objects.get(id = pk)

        previous_purchase = UserPurchase.objects.filter(user = b_user, car = b_car).first()
        if previous_purchase:
            previous_purchase.car_quantity +=1
            previous_purchase.total_price += b_car.price
            previous_purchase.save()
        else:
            new_purchase = UserPurchase(user = b_user, car = b_car, car_quantity = 1, total_price= b_car.price)
            new_purchase.save()
        b_car.quantity -= 1
        b_car.save()
        return redirect('profile')
    else:
        return redirect('homepage')