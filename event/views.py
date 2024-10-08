from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
)
from .models import Post
from .forms import CommentCreationForm


def like_view(request,pk):
    liker = request.user
    # the pk after = is the pk in the parameter
    post = Post.objects.get(pk=pk)
    liked = False
    if post.likes.filter(pk =liker.pk).exists():
        post.likes.remove(liker)
        liked = False
    else:
        post.likes.add(liker)
        liked = True
    # this http_referer goes back to the previous page
    return redirect(request.META.get('HTTP_REFERER'))


def post_list(request):
    
    event = Post.objects.all().order_by('-date')
    context={
        'posts': event,
    }
    return render(request, 'event/main.html',context)

def post_list_bid(request):

    event = Post.objects.all().order_by('-date')
    context={
        'posts': event,
    }
    return render(request, 'event/main.html',context)


def post_comment_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.event_post_comments.all()
    user_comment = None
    if request.method == 'POST':
        comment_form = CommentCreationForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.post = post
            comment_form.save()
            return redirect('/event/post/'+str(pk))
    else:
        comment_form = CommentCreationForm()

    context ={
        'post': post, 
        'comments': comments, 
        'comment_form': comment_form
        }
    return render(request, 'event/post_detail.html', context)


def delete_comment(request,pk):

	# fetch the object related to passed id
	obj = get_object_or_404(Comment,pk=pk)



		# delete object
	obj.delete()
		# after deleting redirect to
		# home page
	return redirect('/event/post/'+str(obj.post.pk))





class PostListView(ListView):
    model = Post
    template_name= 'event/main.html'  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    ordering =['-date']
    paginate_by = 8
    def get_queryset(self):
        return Post.objects.order_by('-date')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','description',]
    success_url = '/event/'

    # override the form_valid method
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# this view seems to be connected with the createView so that
# it does not need an templates
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','description',]

    # override the form_valid method
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # override the method in the userpassesMixin: 
    # only the creator has the access to update
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def delete_view(request,pk):

	# fetch the object related to passed id
	obj = get_object_or_404(Post, pk=pk)

	obj.delete()
		# after deleting redirect to
		# home page
	return redirect('event-home')
