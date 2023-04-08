from django.urls import path, include

from apps.post.views import PostCreateView, UserPostListView, PressLikeView, CommentCreateView, PostDetailView, \
    PostSaveView, HistoryDetailView, NotificationListView, HistoryCeateView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(),name='notifications'),
    path('post-create/',PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('like/<int:post_id>',PressLikeView.as_view(), name='press-like'),
    path('history/<int:pk>',HistoryDetailView.as_view(), name='hisrtory-detail'),
    path('history/craete',HistoryCeateView.as_view(), name='hisrtory-create'),
    path('saved/<int:post_id>', PostSaveView.as_view(), name='post-save'),
    path('post/<post_id>/comment',CommentCreateView.as_view(), name='add-comment'),
]
