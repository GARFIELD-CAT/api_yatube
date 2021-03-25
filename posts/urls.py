from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet


# Создаем роутер.
router = DefaultRouter()
# Связываем URL с viewset.
router.register(r'api/v1/posts', PostViewSet)
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

# Все зарегистрированные в router пути доступны в router.urls.
urlpatterns = [
    path('', include(router.urls)),
]
