from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from schirus.views import UserViewSet
from schirus.views import PostViewSet, CategoryViewSet, LikeViewSet

router = routers.DefaultRouter()


router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('likes', LikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)