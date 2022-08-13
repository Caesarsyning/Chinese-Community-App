from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
)
from . import views as event_views

urlpatterns = [
    path('',login_required(event_views.post_list) ,name='event-home'),
    path('bid',login_required(event_views.post_list_bid) ,name='event-bid'),
    path('post/<int:pk>/', event_views.post_comment_detail,name='event-post-detail'), 
    path('post/new/', PostCreateView.as_view(),name='event-post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='event-post-update'), 
    path('post/<int:pk>/delete/', event_views.delete_view,name='event-post-delete'),
    path('comment/<int:pk>/delete/', event_views.delete_comment ,name='event-comment-delete'), 
    path('post/<int:pk>/like/',event_views.like_view,name='event-post-like'),
]

