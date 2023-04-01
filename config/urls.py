
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('apps.user.urls')),
    path('home/', include('apps.post.urls')),
    path('message/', include('apps.directs.urls')),
]
