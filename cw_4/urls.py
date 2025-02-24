"""
URL configuration for cw_4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

from .views import redirect_to_threads
urlpatterns = [
    path('', views.redirect_to_threads),
    path('threads/', views.threads_list, name='threads_list'),
    path('threads/<int:id>/', views.threads_detail, name='thread_detail'),
    path('threads/<int:id>/delete/', views.thread_delete, name='thread_delete'),
    path('threads/<int:id>/edit/', views.threads_edit, name='thread_edit'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('admin/', admin.site.urls),
    path('', redirect_to_threads, name='home'),  
    path('threads/', include('post.urls')), 
]

