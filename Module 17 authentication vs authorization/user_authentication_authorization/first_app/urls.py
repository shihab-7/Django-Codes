from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.user_logout, name='log_out'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.pswrd_chng, name='change_password'),
    path('change_password2/', views.pswrd_chng2, name='change_password2'),
]
