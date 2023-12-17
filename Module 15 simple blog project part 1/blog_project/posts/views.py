from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})


# edit option setup

def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    # prottek post er primary key diye exact post track rakha hosse
    # print(post.title)
    post_form = forms.PostForm(instance=post)
    # ei line diye agey thekei j data gulo silo oigula save rakha hosse 

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        # instance use korle update kora hok r na hok somossa hobe na ja asa tai thakbe nahoy update korle update hoye jabe
        if post_form.is_valid():
            post_form.save()
            return redirect('home_page')
    return render(request, 'add_post.html', {'form': post_form})


# delete option setup

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home_page')