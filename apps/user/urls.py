from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, CustomLoginView, profile, follow, unfollow, SavedPostView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('mysaved/<username>', SavedPostView.as_view(), name='saved'),
    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('follow/', follow, name='follow'),
    path('unfollow/', unfollow, name='unfollow'),
]