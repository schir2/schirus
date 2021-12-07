from django.urls import path, include

from .views import CustomLoginView, logout_view, UserDetailView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('<slug:username>', UserDetailView.as_view(), name='profile-detail')
]
