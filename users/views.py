from django.contrib.auth.views import auth_login, auth_logout, LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import User


def login_view(request):
    auth_login(request)
    return redirect(reverse_lazy('blog:home'))


def logout_view(request):
    auth_logout(request)
    return redirect(reverse_lazy('blog:home'))


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class UserProfileView(DetailView):
    template_name = 'users/user_profile.html'
    model = User
    slug_url_kwarg = slug_field = 'username'