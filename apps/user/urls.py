from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, CustomLoginView, profile, follow, unfollow

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),

    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('follow/', follow, name='follow'),
    path('unfollow/', unfollow, name='unfollow'),
]