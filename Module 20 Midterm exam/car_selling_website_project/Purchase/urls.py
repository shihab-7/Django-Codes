from django.urls import path
from . import views

urlpatterns = [
    path('purchase/<int:pk>/', views.UserPurchaseView, name='buynow')
]
