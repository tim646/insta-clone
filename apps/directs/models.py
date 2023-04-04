from django.db import models
from django.db.models import Max
from django.utils.crypto import get_random_string

from apps.user.models import User, UserProfile
from apps.common.models import Base

# Create your models here.


class Chat(Base):
    name = models.CharField(max_length=200, null=True, blank=True)

    @property
    def un_read(self):
        return self.messages.filter(is_read=False).count()

    @property
    def un_read_obj(self):
        return self.messages.filter(is_read=False)

    def __str__(self):
        return self.name if self.name else ""

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = get_random_string(20)
        super(Chat, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"


class Participant(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"


class Message(Base):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
