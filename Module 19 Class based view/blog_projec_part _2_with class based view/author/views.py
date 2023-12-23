from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import login, logout, authenticate , update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else :
#         author_form = forms.AuthorForm()
#     return render(request,'add_author.html', {'form': author_form})


def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registration successful')
            return redirect('log_in')
    else :
        register_form = forms.RegistrationForm()
    return render(request,'register.html', {'form': register_form , 'type': 'Register'})


# log in function
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username= user_name, password= user_password)
            if user is not None:
                messages.success(request, 'login successful')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'login information incorrect')
                return redirect('register')

    else:
        form = AuthenticationForm()
    return render(request,'register.html', {'form': form , 'type': 'Login'})


#login function ta class a convert korle
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile') ei attribute kaj kortese na tai methode use korte hobe
    def get_success_url(self):
        return reverse_lazy('profile') 
    # jehetu amra register.html akta template ei login ,register 2 ta kaj e handle korsi tai , login onno template a handle korle oita dite hoito

    # function a validity check er por j messages gulo through kortam oigula class a method use kore kora hoy
    def form_valid(self, form):
        messages.success(self.request, 'login successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'login information incorrect')
        return super().form_invalid(form)
    
    # function a context data diye amra same template a login naki register kaj korbe oita boltam seta eivabe pass korte hoy method use kore
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login' 
        return context
    
        
    

# user profile
@login_required
def profile(request):
    # ei line a author = request.user diye bujhano hoilo j user login asa se e tar post dekhte parbe jeta filter kora hoise
    data = Post.objects.filter(author = request.user) 
    return render(request,'profile.html', {'data': data})


# user password change
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else :
        form = PasswordChangeForm(user= request.user)
    return render(request,'password_change.html', {'form': form })




# user info update
@login_required
def edit_profile(request):
    if request.method == 'POST':
        update_form = forms.ChangeUserDataForm(request.POST, instance= request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Profile Updated successfully')
            return redirect('profile')
    else :
        update_form = forms.ChangeUserDataForm(instance= request.user)
    return render(request,'update_profile.html', {'form': update_form ,})


# user logout
def log_out(request):
    logout(request)
    return redirect('log_in')

# logout view class
# class UserLogoutView(LogoutView):