from django.db.models import ForeignKey, TextField, CASCADE, FileField, Model, DateTimeField, BooleanField, \
    IntegerField, CharField

from apps.common.models import Base
from apps.post.choices import NotoificationChoice
from apps.post.utils import post_upload_path


class Post(Base):
    author = ForeignKey('user.User', on_delete=CASCADE, related_name="posts", default=1)
    body = TextField(null=True, blank=True)
    file = FileField(upload_to=post_upload_path, null=False, blank=False)

    class Meta:
        db_table = "posts"

    @property
    def likes(self):
        return Like.objects.filter(post_id=self.id).count()


class Like(Model):
    user = ForeignKey('user.User', on_delete=CASCADE)
    created = DateTimeField(auto_now=True)
    post = ForeignKey('Post', on_delete=CASCADE, related_query_name='likes')

    class Meta:
        db_table = "likes"


class Comment(Model):
    post = ForeignKey('Post', related_name='comments', on_delete=CASCADE)
    body = TextField(max_length=500, )
    is_reply = BooleanField(default=False)
    author = ForeignKey('user.User', on_delete=CASCADE, related_name='comments')
    created_at = DateTimeField(auto_now_add=True)
    like = IntegerField(default=0)

    class Meta:
        ordering = ['like']
        db_table = "comments"


class Notification(Model):
    user = ForeignKey('user.User', on_delete=CASCADE)
    type = CharField(max_length=22, choices=NotoificationChoice.choices)
    is_seen = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notfications"
        ordering = ['is_seen']
