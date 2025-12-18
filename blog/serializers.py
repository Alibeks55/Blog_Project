from rest_framework import serializers
from .models import  Post, Comment

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields  = [
            'id',
            'author',
            'title',
            'body',
            'created_at',
            'updated_at',
            'is_published'
        ]
        read_only_fields = ['author']

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields  = [
            'id',
            'author',
            'post',
            'body',
            'created_at',
            'updated_at',
            'is_published'
        ]
        read_only_fields = ['author']