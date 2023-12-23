from django.db import models
from categories.models import Category
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
# akta post er multiple categories thakte pare abr akta categorir multiple post thakte pare
    author = models.ForeignKey(User, on_delete= models.CASCADE)
# on delete cascade dile user delete hoye gele post o delete hoye jabe but on delete set null dile post theke jabe just user null hoye jabe
    image = models.ImageField(upload_to ='uploads/' , null=True , blank=True)
    
    def __str__(self):
        return self.title
    

# making a model for comment section using the class based view
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=40)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commented by {self.name}"