from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ChangeUserDataForm
from Purchase.models import UserPurchase
# Create your views here.

@login_required
def profile(request):
    if request.user.is_authenticated:
        info = request.user
        history = UserPurchase.objects.filter(user= request.user)
        return render(request, 'profile.html', {'data': info, 'bought': history})
    else:
        return redirect('login')

class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registration successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Registration unsuccessful')
        return super().form_invalid(form)
    
class UserLoginView(LoginView):
        template_name = 'login.html'
        
        def get_success_url(self):
            return reverse_lazy('profile')

        def form_valid(self, form):
            messages.success(self.request, 'login successful')
            return super().form_valid(form)
        
        def form_invalid(self, form):
            messages.success(self.request, 'login unsuccessful')
            return super().form_invalid(form)
    
    
@method_decorator(login_required , name='dispatch')
class UserLogoutView(LogoutView):

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

@method_decorator(login_required , name='dispatch')
class UserDetailsUpdate(UpdateView):
    template_name = 'update.html'
    form_class= ChangeUserDataForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'User details updated successfully')
        return super().form_valid(form)
    