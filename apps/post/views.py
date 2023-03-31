from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView

from apps.post.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/post_create.html"
    queryset = Post.objects.all()
    fields = ('body', 'file')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(object_list=object_list, **kwargs)
        return context
    template_mame = 'post/posts.html'

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = 'post/post_detail.html'
    model = Post
    context_object_name = "post"
