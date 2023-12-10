from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data, name='data'),
    path('form/', views.form, name='form'),
    # path('django_form/', views.DjangoForm, name='django_form'),
    # path('django_form/', views.StudentForm, name='django_form'),
    path('django_form/', views.Passwordvalidation, name='django_form'),
]
