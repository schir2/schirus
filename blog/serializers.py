from rest_framework import serializers
from blog.models import Category, Like, Post
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email',)


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'url',
            'slug',
            'title',
            'content',
            'subtitle',
            'user',
            'category',
            'like',
            'created_on',
            'updated_on',
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'slug', 'name',)


class LikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'url','post', 'user', 'created_on', 'updated_on',)
