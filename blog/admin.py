from django.contrib import admin
from .models import Category, Post
from .forms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = (
        'title',
        'snippet',
        'graphic',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', )