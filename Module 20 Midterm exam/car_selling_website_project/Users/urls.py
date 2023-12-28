from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update/', views.UserDetailsUpdate.as_view(), name='edit_profile'),
]