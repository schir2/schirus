import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery

from blog.models import Category, Article, Like


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_set = mutations.PasswordSet.Field()
    password_change = mutations.PasswordChange.Field()
    update_account = mutations.UpdateAccount.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()
    remove_secondary_email = mutations.RemoveSecondaryEmail.Field()

    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


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
        filter_fields = ('id', 'user', 'article', 'created_on')
        interfaces = (relay.Node,)


class Query(UserQuery, MeQuery, ObjectType):
    category = relay.Node.Field(CategoryNode)
    categories = DjangoFilterConnectionField(CategoryNode)

    article = relay.Node.Field(ArticleNode)
    articles = DjangoFilterConnectionField(ArticleNode)


class Mutation(AuthMutation, ObjectType):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
