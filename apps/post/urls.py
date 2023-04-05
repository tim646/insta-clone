from django.urls import path, include

from apps.post.views import PostCreateView, UserPostListView, PressLikeView, CommentCreateView, PostDetailView

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('<str:username>/', UserPostListView.as_view(), name="user-posts"),
    # path('create/', PostCreateView.as_view(), name="post-create"),
    path('like/<post_id>',PressLikeView.as_view(), name='press-like'),
    path('post/<post_id>/comment',CommentCreateView.as_view(), name='add-comment')
]
