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
from .models import Post,Comment
from .forms import CommentCreationForm
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline


def post_list(request):
    q = request.GET.get('q')

    if q:
        # where you wanna search
        vector = SearchVector('title','description')
        # what info you are searching for
        query = SearchQuery(q)
        search_headline = SearchHeadline('description',query)
        # housing= Post.objects.annotate(search=vector).filter(search=query)
        # housing= Post.objects.annotate(rank=SearchRank(vector,query)).annotate(headline=search_headline).filter(rank__gte=0.001).order_by('-rank')
        housing = Post.objects.filter(title__icontains=q)
    else:
        housing = Post.objects.filter(post_category='ask').order_by('-date')
    context={
        'posts': housing,
    }
    return render(request, 'housing/main.html',context)

def post_list_bid(request):
    q = request.GET.get('q')

    if q:
        # where you wanna search
        vector = SearchVector('title','description')
        # what info you are searching for
        query = SearchQuery(q)
        search_headline = SearchHeadline('description',query)
        # housing= Post.objects.annotate(search=vector).filter(search=query)
        # housing= Post.objects.annotate(rank=SearchRank(vector,query)).annotate(headline=search_headline).filter(rank__gte=0.001).order_by('-rank')
        housing = Post.objects.filter(title__icontains=q)
    else:
        housing = Post.objects.filter(post_category='bid').order_by('-date')
    context={
        'posts': housing,
    }
    return render(request, 'housing/main.html',context)


def post_comment_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.housing_post_comments.all()
    user_comment = None
    if request.method == 'POST':
        comment_form = CommentCreationForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.post = post
            comment_form.save()
            return redirect('/housing/post/'+str(pk))
    else:
        comment_form = CommentCreationForm()

    context ={
        'post': post, 
        'comments': comments, 
        'comment_form': comment_form
        }
    return render(request, 'housing/post_detail.html', context)


def delete_comment(request,pk):

	# fetch the object related to passed id
	obj = get_object_or_404(Comment,pk=pk)



		# delete object
	obj.delete()
		# after deleting redirect to
		# home page
	return redirect('/housing/post/'+str(obj.post.pk))




class PostListView(ListView):
    model = Post
    template_name= 'housing/main.html'  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    ordering =['-date']
    paginate_by = 8
    def get_queryset(self):
        return Post.objects.filter(post_category='ask').order_by('-date')

class PostListViewBid(ListView):
    model = Post
    template_name= 'housing/main.html'  #<app>/<model>_<viewtype>.html
    context_object_name ="posts"
    ordering =['-date']
    paginate_by = 8
    def get_queryset(self):
        return Post.objects.filter(post_category='bid').order_by('-date')


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','post_category','description','sold']
    success_url = '/housing/'

    # override the form_valid method
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# this view seems to be connected with the createView so that
# it does not need an templates
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','post_category','description','sold']

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
	return redirect('housing-home')
