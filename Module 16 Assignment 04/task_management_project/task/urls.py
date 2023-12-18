from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='Add Task'),
    path('edit/<int:id>', views.edit_task, name='Edit Task'),
    path('delete/<int:id>', views.delete_task, name='Delete Task'),
]
