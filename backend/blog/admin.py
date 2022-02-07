from django.contrib import admin

from .models import Category, Article, Like


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ...
