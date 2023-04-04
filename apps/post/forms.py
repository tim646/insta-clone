from django.forms import ModelForm
from apps.post.models import Post, Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
