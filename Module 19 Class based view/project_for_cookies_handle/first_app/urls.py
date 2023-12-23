from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name= 'homepage'),
    path('', views.set_session, name= 'homepage'),
    # path('get/', views.get_cookie, name= 'cookies'),
    path('get/', views.get_session, name= 'cookies'),
    # path('del/', views.delete_cookie, name= 'cookie_deleted'),
    path('del/', views.delete_session, name= 'cookie_deleted'),
]
