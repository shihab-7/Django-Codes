from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django import forms


class RegisterForm(UserCreationForm):

# django theke forms k import kore nicher moto manually widgets set kore deowa jay shubidha moto 

    first_name = forms.CharField(widget= forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={'id': 'required'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'id': 'required'}))
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'first_name', 'last_name']

# user update   form
        
class UpdateInfoForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        # fields= '__all__'
        fields = ['username', 'email', 'first_name', 'last_name']