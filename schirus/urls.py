from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from main.views import redirect_to_blog_view

urlpatterns = [
    path('', redirect_to_blog_view),
    path('admin/', admin.site.urls),
    path('accounts/', include(('allauth.urls', 'allauth'), namespace='allauth')),
    path('login/', TemplateView.as_view(template_name='users/login.html')),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)