from django.db import models
from category.models import CategoryModel
# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=100)
    task_Description = models.TextField()
    is_completed = models.BooleanField(default=False)
    Assigning_Date= models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return f"{self.task_title}"