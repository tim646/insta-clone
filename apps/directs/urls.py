from django.urls import path

from apps.directs import views
from apps.directs.views import MessageView, create_chat

urlpatterns = [
    path('', views.inbox, name='message'),
    path('<str:name>/', views.inbox, name='message'),
    path("create_chat/<str:user_id>/", views.create_chat, name='create-chat'),

    ## socket
    path("chat/", MessageView.as_view(), name='chat'),
    path("chat/<str:name>/", MessageView.as_view(), name='chat'),
    path("create_chat/<str:user_id>/", create_chat, name='create-chat'),

    path('directs/<username>', views.Directs, name='directs'),
    path('send/', views.SendMessage, name='send-message'),
    path('search/', views.UserSearch, name="search-users"),
    path('new/<username>', views.NewConversation, name="conversation"),
]
