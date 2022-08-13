from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


@login_required
def home(request):
    return render(request,'home/home.html',context={'user':request.user})


