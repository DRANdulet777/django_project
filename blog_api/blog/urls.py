from django.urls import path, include
from . import views  # Импорт HTML views
from .api_views import PostViewSet, CommentViewSet  # Импорт API views
from rest_framework.routers import DefaultRouter


# Создание роутера для API
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # HTML Views
    path('', views.post_list, name='post_list'),  # Список постов
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Детали поста
    path('post/new/', views.post_create, name='post_create'),  # Создание нового поста
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # Редактирование поста
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  # Удаление поста

    # API Views
    path('api/', include(router.urls)),  # Подключение роутера для API
]
