from django.urls import path

from apps.directs import views

urlpatterns = [
    path('', views.inbox, name='message'),
    path('<str:name>/', views.inbox, name='message'),
    path("create_chat/<str:user_id>/", views.create_chat, name='create-chat'),

    path('directs/<username>', views.Directs, name='directs'),
    path('send/', views.SendMessage, name='send-message'),
    path('search/', views.UserSearch, name="search-users"),
    path('new/<username>', views.NewConversation, name="conversation"),
]
