from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# def confirm(request):
#     return HttpResponse('<p>cTsrODfB9qJ3wpWYifX4HEsjpeTFfXxjMAijs-U0bOc.HIrdzCNgiv-X0ysWoBH3t5nB7ioPPpJPyQrYnf7XqAs</p>')

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html',context)


class PostListView(ListView):
    model = Post
    template_name= 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    ordering =['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name= 'blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    ordering =['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    # override the form_valid method
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# this view seems to be connected with the createView so that
# it does not need an templates
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    # override the form_valid method
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # override the method in the userpassesMixin: 
    # only the creator has the access to update
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url ='/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})

