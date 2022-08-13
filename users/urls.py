
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from . import views as user_views



urlpatterns = [
    path('profile/<int:pk>/',user_views.post_view,name="profile"),
    path('profile/<int:pk>/likes',user_views.likes_view,name="profile-likes"),
    path('profile/<int:pk>/update',user_views.profile_update,name="profile_update"),
    path('logout/',user_views.logout_view,name="logout"),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name ='user/password_reset.html'),
        name="password_reset"),
    path('password-reset/done',
        auth_views.PasswordResetDoneView.as_view(template_name ='user/password_reset_done.html'),
        name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name ='user/password_reset_confirm.html'),
        name="password_reset_confirm"),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name ='user/password_reset_complete.html'),
        name="password_reset_complete")
]


