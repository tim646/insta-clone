
from django.contrib import admin
from django.urls import path, include

from apps.common.views import HomeView

urlpatterns = [
    path('home/',HomeView.as_view(),name="home" ),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('apps.user.urls')),
    path('posts/', include('apps.post.urls')),
    path('admin/', admin.site.urls),

]
