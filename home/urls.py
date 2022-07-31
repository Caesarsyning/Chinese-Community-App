from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from . import views as home_view


urlpatterns = [
    path('', home_view.home,name='home'),
    # path('user/<str:username>',UserPostListView.as_view() ,name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'), 
    # path('post/new/', PostCreateView.as_view(),name='post-create'), 
    # path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'), 
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'), 
    # path('about/', views.about,name='blog-about'), 
]
