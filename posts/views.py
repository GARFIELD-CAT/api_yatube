from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer


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
    # Поле post будет взято из переменной url post_id.
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')  # Получаем id поста.
        post = get_object_or_404(Post, id=post_id)  # Делаем запрос к базе.
        serializer.save(author=self.request.user, post=post)

    # Queryset будет собран из комментариев одного поста.
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')  # Получаем id поста.
        post = get_object_or_404(Post, id=post_id)  # Делаем запрос к базе.
        # Выводим все комментарии поста через related_name.
        return post.comments.all()
