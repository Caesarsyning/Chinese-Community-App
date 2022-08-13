from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
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
from housing import models as housing_models
from resale import models as resale_models
from course import models as course_models
from event import models as event_models

@login_required
def post_view(request,pk):
    author = User.objects.get(pk=pk)
    housing_post = author.housing_author_posts.all().order_by('-date')
    course_post = author.course_author_posts.all().order_by('-date')
    resale_post = author.resale_author_posts.all().order_by('-date')
    event_post = author.event_author_posts.all().order_by('-date')
    context = {
        'housing_post':housing_post,
        'course_post':course_post,
        'resale_post':resale_post,
        'event_post':event_post,
        'author':author,
    }
    return render(request,'user/post_view.html',context)

@login_required
def likes_view(request,pk):
    author = User.objects.get(pk=pk)
    
    housing_post = author.housing_like_posts.all().order_by('-date')
    course_post = author.course_like_posts.all().order_by('-date')
    resale_post = author.resale_like_posts.all().order_by('-date')
    event_post = author.event_like_posts.all().order_by('-date')
    context = {
        'housing_post':housing_post,
        'course_post':course_post,
        'resale_post':resale_post,
        'event_post':event_post,
        'author':author,
    }
    return render(request,'user/post_view.html',context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('account_login')



# we want to require login before viewing the profile page
# this will direct to the default login route, we need to set it the login url in the setting
@login_required
def profile_update(request,pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance =request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile',pk=pk)
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
   
    context ={
        'u_form' : u_form,
        'p_form' : p_form,
    }

    return render(request,'user/profile_update.html',context)











