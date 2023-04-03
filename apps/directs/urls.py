from django.urls import path
from apps.directs import views

urlpatterns = [
    path('', views.inbox, name='message'),
    path('direct/<username>', views.Directs, name='directs'),
    path('send/', views.SendMessage, name='send-message'),
    path('search/', views.UserSearch, name="search-users"),
    path('new/<username>', views.NewConversation, name="conversation"),
]