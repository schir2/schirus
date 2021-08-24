from django.urls import path, include

from blog.views import CategoryAutoCompleteView
from blog.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView, LikePostView

urlpatterns = [
    path('category', CategoryAutoCompleteView.as_view(create_field='name'), name='category-autocomplete'),
    path('', PostListView.as_view(), name='post-list'),
    path('', PostListView.as_view(), name='home'),
    path('create', PostCreateView.as_view(), name='post-create'),
    path('<str:slug>-<int:pk>/', include([
        path('', PostDetailView.as_view(), name='post-detail'),
        path('update', PostUpdateView.as_view(), name='post-update'),
        path('delete', PostDeleteView.as_view(), name='post-delete'),
        path('like', LikePostView.as_view(), name='post-like'),
    ]))
]
