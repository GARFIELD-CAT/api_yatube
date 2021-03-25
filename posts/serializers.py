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
    # В ответе на запрос поле post будет выведено как Key.
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('author',)
