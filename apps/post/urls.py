from django.urls import path, include

from apps.post.views import PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<pk>', PostDetailView.as_view(), name="post"),
    path('post-create/', PostCreateView.as_view(), name="post_create"),

]
