import graphene
from django.contrib.auth import get_user_model
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from blog.models import Category, Article, Like


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ('id', 'name', 'slug')
        interfaces = (relay.Node,)


class ArticleNode(DjangoObjectType):
    class Meta:
        model = Article
        filter_fields = ('id', 'slug', 'title', 'content', 'user', 'categories', 'likes', 'created_on', 'updated_on')
        interfaces = (relay.Node,)


class LikeNode(DjangoObjectType):
    class Meta:
        model = Like
        filter_fields = ('id', 'user', 'article', 'created_on', 'updated_on')
        interfaces = (relay.Node,)


class UserNode(DjangoObjectType):
    class Meta:
        model = get_user_model()
        filter_fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'likes')
        interfaces = (relay.Node,)


class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    article = relay.Node.Field(ArticleNode)
    all_articles = DjangoFilterConnectionField(ArticleNode)

    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)


schema = graphene.Schema(query=Query)
