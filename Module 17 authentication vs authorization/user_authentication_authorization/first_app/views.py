from django.shortcuts import render,redirect
from .forms import RegisterForm , UpdateInfoForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate , login, logout, update_session_auth_hash
# Create your views here.

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if not request.user.is_authenticated:
        # eita diye user jodi valid hoy tobe r sign up page dekhte parbe na ei system ta kore hoilo
        if request.method == 'POST':
            form = RegisterForm( request.POST )
            if form.is_valid():
                messages.success(request, "Account created successfully")
                # messages.warning(request, "Account created successfully")
                # messages.info(request, "Account created successfully")
                form.save()
                # print(form.cleaned_data)
                return redirect('log_in')
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form':form})
    else:
        return redirect('profile')


def log_in(request):
    if not request.user.is_authenticated:
        # eita diye user jodi valid hoy tobe r login option dekhte parbe na ei system ta kore hoilo
        if request.method == 'POST':
            form = AuthenticationForm(request= request, data= request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                pswrd = form.cleaned_data['password']
                user = authenticate(username = name, password = pswrd)
                # authenticate diye check kora hosse j user database a asa ki na
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        return redirect('profile')  

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateInfoForm( request.POST , instance= request.user )
            if form.is_valid():
                messages.success(request, "Account updated successfully")
                form.save()
                # print(form.cleaned_data)
                return redirect('profile')
        else:
            form = UpdateInfoForm(instance= request.user)
        return render(request, 'profile.html', {'form':form})
    else:
        return redirect('sign_up')
    

# def profile(request):
#     if request.user.is_authenticated:
#         return render(request, 'profile.html', {'user': request.user})
#     else:
#         return redirect('log_in')

def user_logout(request):
    logout(request)
    return redirect('log_in')

def pswrd_chng(request):
    if  request.user.is_authenticated:
        if request.method=='POST':
            form = PasswordChangeForm(user= request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                # password k hash a convert kore database a update kore dibe
                return redirect('profile')
        else:
            form = PasswordChangeForm(user= request.user)
        return render(request, 'change_password.html',{'form':form})
    else:
        return redirect('log_in')

def pswrd_chng2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user= request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user= request.user)
        return render(request, 'change_password.html',{'form':form})
    else:
        return redirect('log_in')


# user info update
# def user_update(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = UpdateInfoForm( request.POST , instance= request.user )
#             if form.is_valid():
#                 messages.success(request, "Account updated successfully")
#                 form.save()
#                 # print(form.cleaned_data)
#                 return redirect('profile')
#         else:
#             form = UpdateInfoForm()
#         return render(request, 'profile.html', {'form':form})
#     else:
#         return redirect('sign_up')