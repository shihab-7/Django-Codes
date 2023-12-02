# eita banay nite hoise

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path('contact/', views.contact),
    path('courses/', views.courses)
]

# ei first app ta k abr project er url er path a add kore dite hobe
