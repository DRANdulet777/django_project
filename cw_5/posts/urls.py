from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostCreateView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.post_list, name='post_list'),  # Было 'posts/', стало ''
    path('my/', views.my_posts, name='my_posts'),  # Было 'posts/my/', стало 'my/'
    path('create/', PostCreateView.as_view(), name='post_create'),
]
