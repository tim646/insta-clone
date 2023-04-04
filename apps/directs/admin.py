from django.contrib import admin
from .models import Message, Participant, Chat
# Register your models here.

admin.site.register(Chat)
admin.site.register(Participant)
admin.site.register(Message)