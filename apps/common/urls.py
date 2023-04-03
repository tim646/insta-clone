from django.urls import path, include

from apps.common.views import HomeView, PressLikeView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path('like/<post_id>',PressLikeView.as_view(), name='press-like')
]
