from django.urls import path, include

from apps.post.views import PostCreateView, PostListView

urlpatterns = [
    path('post-create/', PostCreateView.as_view(), name="post_create"),
    path('home/', PostListView.as_view(), name="home")
]
