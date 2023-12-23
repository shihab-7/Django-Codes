from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    # path('log_in/', views.log_in, name='log_in'),
    path('log_in/', views.UserLoginView.as_view(), name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    # path('log_out/', views.UserLogoutView.as_view(), name='log_out'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('update/', views.change_password, name='update'),
]
