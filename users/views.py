from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterform, ProfileUpdateForm, UserUpdateForm

from django.http import HttpResponse



def logout_view(request):
    logout(request)
    messages.success(request,f'Your account has been logged out.')
    return redirect('login')

@login_required
def home(request):
    return render(request,'user/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created!')
            new_user = authenticate(username=username,password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect('home')
    else:       
        form = UserRegisterform()
    return render(request,'user/register.html',{'form':form})




# we want to require login before viewing the profile page
# this will direct to the default login route, we need to set it the login url in the setting
@login_required
def profile(request):
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
        'p_form' : p_form
    }

    return render(request,'user/profile.html',context)










