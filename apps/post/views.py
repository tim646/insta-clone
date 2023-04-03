from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from apps.post.forms import PostCreateForm
from apps.post.models import Post
from apps.user.models import User


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/post_create.html"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserPostListView(LoginRequiredMixin, DetailView):
    queryset = Post.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

    template_mame = 'myprofile.html'


# class PostDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'post/post_detail.html'
#     model = Post
#     context_object_name = "post"
