from django.contrib import admin
from .models import Category, Article, Like


admin.register(Article)
admin.register(Category)
admin.register(Like)
