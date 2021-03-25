from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post
from .serializers import CommentSerializer, PostSerializer


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Пользовательское разрешение на уровне объекта.
    Проверяет, что действие совершает автор, если не он,
    то разрешены только безопасные запросы.
    '''
    def has_object_permission(self, request, view, obj):
        # Разрешены GET, HEAD, OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Для остальных запросы может делать только автор объекта.
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # При создании поста поле author будет взято из request.user.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    # При создании комментария поле author будет взято из request.user.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # Queryset будет собран из комментариев одного поста.
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')  # Получаем id поста.
        post = Post.objects.get(id=post_id)  # Делаем запрос к базе.
        # Выводим все комментарии поста через related_name.
        return post.comments.all()
