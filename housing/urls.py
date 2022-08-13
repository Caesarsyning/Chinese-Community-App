from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
)
from . import views as housing_views

urlpatterns = [
    path('',login_required(housing_views.post_list) ,name='housing-home'),
    path('bid',login_required(housing_views.post_list_bid) ,name='housing-bid'),
    path('post/<int:pk>/', housing_views.post_comment_detail,name='housing-post-detail'), 
    path('post/new/', PostCreateView.as_view(),name='housing-post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='housing-post-update'), 
    path('post/<int:pk>/delete/', housing_views.delete_view,name='housing-post-delete'),
    path('comment/<int:pk>/delete/', housing_views.delete_comment ,name='housing-comment-delete'), 
    path('post/<int:pk>/like/',housing_views.like_view,name='housing-post-like'),
]
