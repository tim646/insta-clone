
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from apps.common.views import HomeView

from allauth.socialaccount import views as socialaccount_views

urlpatterns = [
    path('home/',HomeView.as_view(),name="home" ),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.user.urls')),

    path('message/', include('apps.directs.urls')),
    path('posts/', include('apps.post.urls')),
    path('admin/', admin.site.urls),
    path('template1', TemplateView.as_view(template_name='messenger.html')),

]
