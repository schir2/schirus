from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from main.views import redirect_to_blog_view
from rest_framework import routers
from blog.viewsets import UserViewSet, PostViewSet, CategoryViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'blog', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', redirect_to_blog_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)