from django.urls import path, include

from .views import CustomLoginView, logout_view, UserProfileView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('<slug:username>', UserProfileView.as_view(), name='user-profile')
]
