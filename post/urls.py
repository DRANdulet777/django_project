from django.urls import path
from . import views

urlpatterns = [
    path('', views.threads_list, name='thread_list'),  # Главная страница с тредами
]
