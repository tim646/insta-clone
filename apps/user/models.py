from django.db import models
from apps.common.models import Base
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="profile_picture", null=False, default="default.jpg")

    # is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserProfile(Base):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="profile_picture", null=False, default="default.jpg")

    def follow(self, user):
        self.user.followings.add(user)

    def unfollow(self, user):
        self.user.followings.remove(user)

    def save(self, *args, **kwargs):
        if self.pk:
            # Update the associated User instance if the profile has been updated
            self.user.first_name = self.first_name
            self.user.last_name = self.last_name
            self.user.image = self.image
            self.user.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.user.username


class Saved(models.Model):
    user = models.ForeignKey('user.User', models.CASCADE)
    post = models.ForeignKey('post.Post', models.CASCADE)

    class Mete:
        db_table = 'saved'
        uniqeu_togather = ['user', 'post']
        verbose_name = 'Saved'
        verbose_name_plural = 'Saved'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.save()








