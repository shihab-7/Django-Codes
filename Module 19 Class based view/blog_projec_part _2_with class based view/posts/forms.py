from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['author']


# making form to show the comment model in frontend

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['name', 'email', 'body']