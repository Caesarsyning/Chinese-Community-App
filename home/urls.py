from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from . import views as home_view



urlpatterns = [
    path('', home_view.home,name='home'),
]
