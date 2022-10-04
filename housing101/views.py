
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
)

from .models import Post,offPost


# Create your views here.
def home(request):
    return render(request,'housing101/home.html',context={'user':request.user})


class PostListView(ListView):
    model = Post
    template_name= 'housing101/on.html'  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    paginate_by = 8


class offPostListView(ListView):
    model = offPost
    template_name= 'housing101/off.html'  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    paginate_by = 8


