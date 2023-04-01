from django.forms import ModelForm
from apps.post.models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)