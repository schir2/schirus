from django.contrib import admin
from .models import Category, Post, Like
from .forms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = (
        'title',
        'snippet',
        'like_count',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', )


@admin.register(Like)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created_on', 'updated_on',)