from typing import Any
from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():

            # ei line diye bujhay j user currently login asa shei user post kortese
            post_form.instance.author = request.user 
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})

# add_post function ta class a convert kore class based view toiri kore same kaj kora jay
@method_decorator(login_required, name= 'dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


# edit option setup
@login_required
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
            post_form.instance.author = request.user
            post_form.save()
            return redirect('home_page')
    return render(request, 'add_post.html', {'form': post_form})

# Edit function er kaj UpdateView diye kora jay
@method_decorator(login_required, name= 'dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home_page')

# delete option setup
@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('home_page')

# delete function er kaj DeleteView diye kora jay
@method_decorator(login_required, name= 'dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


# class based view for post details card

class PostDetailsView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    # akhon prottek post er jonno  kono user comment korle seta show korte plus dekhanor jonno j method lage oita

    # class based view te function er moto kore post handle kora jay na eivabe method banay niye handle korte hoy
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    

#  eikhane comment ta ke context data hishebe frontend a pass kora hoilo.
    def get_context_data(self, **kwargs):

        context= super().get_context_data(**kwargs)
        post = self.object # post model er object gulo store kora hoise
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
