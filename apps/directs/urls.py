from django.urls import path
from apps.directs import views

urlpatterns = [
    path('', views.inbox, name='message'),
    path('direct/<username>', views.Directs, name='directs'),
]