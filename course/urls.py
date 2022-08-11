from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
)
from . import views as course_views

urlpatterns = [
    path('',login_required(course_views.post_list) ,name='course-home'),
    path('bid',login_required(course_views.post_list_bid) ,name='course-bid'),
    path('post/<int:pk>/', course_views.post_comment_detail,name='course-post-detail'), 
    path('post/new/', PostCreateView.as_view(),name='course-post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='course-post-update'), 
    path('post/<int:pk>/delete/', course_views.delete_view,name='course-post-delete'),
    path('comment/<int:pk>/delete/', course_views.delete_comment ,name='course-comment-delete'), 
]

