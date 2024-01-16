from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ServiceViews

router = DefaultRouter()
router.register('' , ServiceViews)

urlpatterns = [
    path('', include(router.urls))
]