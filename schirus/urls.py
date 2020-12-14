from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login/', TemplateView.as_view(template_name='users/login.html')),
]
