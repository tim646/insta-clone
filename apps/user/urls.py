from django.urls import path
from .views import SignUpView, CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),


]