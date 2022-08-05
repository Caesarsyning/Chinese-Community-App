from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterform, 
    ProfileUpdateForm, 
    UserUpdateForm, 
    MyCustomLoginForm
)

from django.http import HttpResponse



def logout_view(request):
    logout(request)
    return redirect('account_login')


def profile(request):
    return render(request,'user/profile.html')

# we want to require login before viewing the profile page
# this will direct to the default login route, we need to set it the login url in the setting
@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance =request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
   
    context ={
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request,'user/profile_update.html',context)











