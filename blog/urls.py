from django.urls import path, include

from blog.views import CategoryAutoCompleteView
from blog.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('category', CategoryAutoCompleteView.as_view(create_field='name'), name='category-autocomplete'),
    path('posts/', include([
        path('', PostListView.as_view(), name='post-list'),
        path('<int:pk>-<str:slug>/', PostDetailView.as_view(), name='post-detail'),
        path('create', PostCreateView.as_view(), name='post-create'),
    ]))
]
