from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from config import settings

urlpatterns = [
    path('home/',HomeView.as_view(),name="home" ),
    path('accounts/', include('allauth.urls')),
    path('posts/', include('apps.post.urls')),
    path('home/', include('apps.common.urls')),
    path('', include('apps.user.urls')),

    path('message/', include('apps.directs.urls')),
    path('admin/', admin.site.urls),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
