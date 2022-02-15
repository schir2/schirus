import graphene
from django.contrib.auth import get_user_model
from graphene import ObjectType
from graphene_django import DjangoListField
from graphene_django import DjangoObjectType
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


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class LikeType(DjangoObjectType):
    class Meta:
        model = Like
        fields = ('id', 'user', 'article', 'created_on')


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',
            'groups')


class ArticleType(DjangoObjectType):
    user = UserType
    likes = DjangoListField(LikeType)

    class Meta:
        model = Article
        fields = ('id', 'slug', 'title', 'content', 'user', 'likes', 'categories', 'created_on', 'updated_on')


class Query(UserQuery, MeQuery, ObjectType):
    categories = DjangoListField(CategoryType)
    articles = DjangoListField(ArticleType)
    users = DjangoListField(UserType)


class Mutation(AuthMutation, ObjectType):
    ...


schema = graphene.Schema(query=Query, mutation=Mutation)
