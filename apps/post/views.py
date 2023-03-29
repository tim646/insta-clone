from django.shortcuts import render
from django.views.generic import CreateView, ListView

from apps.post.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('body', 'file')
    template_name = 'post_create.html'
    success_url = 'posts'

#
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_mame = 'index.html'