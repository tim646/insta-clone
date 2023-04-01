from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from apps.post.models import Post, Like, PostMedia, Comment, Notification


class PostMediaInline(StackedInline):
    model = PostMedia
    extra = 1
@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    inlines = (PostMediaInline,)


@admin.register(Like)
class LikeAdmin(ModelAdmin):
    list_display = ['post', 'user']

admin.site.register([ Comment, Notification])