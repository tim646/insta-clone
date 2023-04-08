from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, CustomLoginView, UserProfileView, follow, unfollow, SavedPostView, edit_profile

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('mysaved/<username>', SavedPostView.as_view(), name='saved'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('follow/<int:pk>/', follow, name='follow'),
    path('unfollow/<int:pk>/', unfollow, name='unfollow'),
]