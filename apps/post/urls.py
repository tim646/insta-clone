from django.urls import path, include

from apps.post.views import PostCreateView, UserPostListView

urlpatterns = [
    path('<pk>/', UserPostListView.as_view(), name="user_posts"),
    path('create/', PostCreateView.as_view(), name="post_create"),

]
