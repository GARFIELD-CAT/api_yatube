from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    # В ответе на запрос поле author будет выведено на основе своей __str__.
    author = serializers.StringRelatedField()

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        # Если ставим read_only_fields, то не ожидаем их ввода в запросе,
        # а сами заполняем их значения у обязательных полей.
        read_only_fields = ('author', 'post')
