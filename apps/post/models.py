from django.db.models import ForeignKey, TextField, CASCADE, FileField, Model, DateTimeField

from apps.common.models import Base
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
