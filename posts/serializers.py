from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    # В ответе поле author будет выведено на основе данных поля username.
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    # В ответе поле author будет выведено на основе данных поля username.
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        # Если ставим read_only_fields, то не ожидаем их ввода в запросе,
        # а сами заполняем их значения у обязательных полей.
        read_only_fields = ('post',)
