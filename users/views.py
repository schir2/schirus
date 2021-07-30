from django.contrib.auth.views import auth_login, auth_logout, LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Profile, User


def login_view(request):
    auth_login(request)
    return redirect(reverse_lazy('blog:home'))


def logout_view(request):
    auth_logout(request)
    return redirect(reverse_lazy('blog:home'))


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class UserDetailView(DetailView):
    template_name_suffix = '_detail'
    model = User
    slug_url_kwarg = slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.name.title()}"
        return context