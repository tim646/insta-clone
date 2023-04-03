from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),

    path('register/', SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

]