from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from main.views import redirect_to_blog_view
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', redirect_to_blog_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)