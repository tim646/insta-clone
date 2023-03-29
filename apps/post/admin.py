from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.post.models import Post, Like


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['body', 'author', 'file', 'created_at']

@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = ['post', 'user']
