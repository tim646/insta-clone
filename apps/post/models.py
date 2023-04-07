from django.db.models import ForeignKey, CASCADE, FileField, Model, DateTimeField, BooleanField, \
    CharField, ManyToManyField

from apps.common.models import Base
from apps.post.choices import NotoificationChoice
from apps.post.utils import post_upload_path, validate_file_extension, history_upload_path


class Post(Base):
    author = ForeignKey('user.User', CASCADE,"posts")
    title = CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "posts"

    @property
    def like_count(self):
        return Like.objects.filter(post_id=self.id).count()

    @property
    def medias(self):
        return PostMedia.objects.filter(post_id=self.id)

    @property
    def comment_count(self):
        return Comment.objects.filter(post_id=self.id).count()


class PostMedia(Model):
    file = FileField(upload_to=post_upload_path, null=False, blank=False,
                     validators=[validate_file_extension, ])
    post = ForeignKey('post.Post', CASCADE, "post_medias")


class Like(Model):
    user = ForeignKey('user.User', CASCADE)
    created = DateTimeField(auto_now=True)
    post = ForeignKey('Post', on_delete=CASCADE, related_name='likes')

    class Meta:
        db_table = "likes"
        unique_together = ('user', 'post')


class Comment(Model):
    post = ForeignKey('Post', CASCADE, 'comments')
    body = CharField(max_length=500)
    author = ForeignKey('user.User', CASCADE, 'comments')
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"


class Notification(Model):
    user = ForeignKey('user.User', CASCADE)
    type = CharField(max_length=22, choices=NotoificationChoice.choices)
    is_seen = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notfications"
        ordering = ['-created_at', 'is_seen']


class History(Model):
    author = ForeignKey('user.User', CASCADE,'histories')
    seen_by = ManyToManyField('user.User','seen_by', blank=True)
    file = FileField(validators=[validate_file_extension,], upload_to=history_upload_path)
    created_at = DateTimeField(auto_now_add=True)


    def mark_seen(self, user):
        self.seen_by.add(user)
        self.save()
    class Meta:
        db_table = 'history'
        verbose_name = 'History'
        verbose_name_plural = 'Histories'

