from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, CustomLoginView, edit_profile, follow, unfollow, show_followings, show_followers, SavedPostView, UserDetailView


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('mysaved/<username>/', SavedPostView.as_view(), name='saved'),
    path('profile/<username>/', UserDetailView.as_view(), name='user-profile'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('edit/profile/', edit_profile, name='edit_profile'),
    path('follow/<int:pk>/', follow, name='follow'),
    path('unfollow/<int:pk>/', unfollow, name='unfollow'),
     path('profile/followings/<username>/', show_followings, name='show_followings'),
     path('profile/followers/<username>/', show_followers, name='show_followers'),
]