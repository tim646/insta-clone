from django.db import models
from apps.common.models import Base
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followings', symmetrical=False)
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(Base):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_picture", null=True, default="default.jpg")
    full_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

