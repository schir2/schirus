from rest_framework import viewsets
from blog.serializers import CategorySerializer, LikeSerializer, PostSerializer, UserSerializer
from blog.models import Category, Like, Post
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()