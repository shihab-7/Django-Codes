from django.shortcuts import render, redirect
from Cars.models import Car
from CarBrands.models import Brands

def home(request, brand_slug= None):
    data = Car.objects.all()

    if brand_slug is not None:
        brand = Brands.objects.get(slug = brand_slug)
        data = Car.objects.filter(brand = brand)
    
    brands = Brands.objects.all()
    return render(request,'home.html',{'data':data, 'brand': brands})
