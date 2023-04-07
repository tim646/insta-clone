
from django import forms

from django.forms.models import inlineformset_factory
from .models import Post, PostMedia

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']

PostMediaFormSet = inlineformset_factory(Post, PostMedia, fields=['file'], extra=1)
