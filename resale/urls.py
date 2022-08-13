from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostListViewBid
)
from . import views as resale_views

urlpatterns = [
    path('',login_required(resale_views.post_list) ,name='resale-home'),
    path('bid',login_required(resale_views.post_list_bid) ,name='resale-bid'),
    path('post/<int:pk>/', resale_views.post_comment_detail,name='resale-post-detail'), 
    path('post/new/', PostCreateView.as_view(),name='resale-post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='resale-post-update'), 
    path('post/<int:pk>/delete/', resale_views.delete_view ,name='resale-post-delete'), 
    path('comment/<int:pk>/delete/', resale_views.delete_comment ,name='resale-comment-delete'), 
    path('post/<int:pk>/like/',resale_views.like_view,name='resale-post-like'),
]
