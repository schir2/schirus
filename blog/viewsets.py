from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=True)
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        print(post.like)
        print(request.user)
        return Response(self.serializer_class(instance=post, context={'request':request}).data, )


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()