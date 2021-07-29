from django.urls import path, include

from blog.views import CategoryAutoCompleteView
from blog.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, like_post_view

urlpatterns = [
    path('category', CategoryAutoCompleteView.as_view(create_field='name'), name='category-autocomplete'),
    path('', PostListView.as_view(), name='post-list'),
    path('', PostListView.as_view(), name='home'),
    path('create', PostCreateView.as_view(), name='post-create'),
    path('like', like_post_view, name='post-like'),
    path('<int:pk>-<str:slug>/', include([
        path('', PostDetailView.as_view(), name='post-detail'),
        path('update', PostUpdateView.as_view(), name='post-update'),
        path('delete', PostDeleteView.as_view(), name='post-delete'),
    ]))
]
