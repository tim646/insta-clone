from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User, Saved

# Register your models here.

admin.site.register(UserProfile)
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ['username', ]

@admin.register(Saved)
class SavedAdmin(ModelAdmin):
    list_display = ['user', 'post']