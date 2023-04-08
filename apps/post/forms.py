from django.forms import ModelForm, ClearableFileInput

from django.forms.models import inlineformset_factory
from .models import Post, PostMedia, History


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title']


PostMediaFormSet = inlineformset_factory(Post, PostMedia, fields=['file'], extra=1)


class HistoryCreateForm(ModelForm):
    class Meta:
        model = History
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }
