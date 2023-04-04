from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, TemplateView

from apps.post.choices import NotoificationChoice
from apps.post.forms import PostCreateForm
from apps.post.models import Post, Like, Notification, Comment
from apps.user.models import User


class PressLikeView(View, LoginRequiredMixin):
    def get(self, request, post_id):
        like, created = Like.objects.get_or_create(post_id=post_id, user=request.user)
        if not created:
            like.delete()
        if created and not Notification.objects.filter(user=request.user, type=NotoificationChoice.LIKE).exists():
            Notification.objects.create(user=request.user, type=NotoificationChoice.LIKE)

        return redirect('home')


class CommentCreateView(View, LoginRequiredMixin):
    def post(self, request, post_id):
        Comment.objects.create(post_id=post_id, body=request.POST['comment'], author=self.request.user)
        Notification.objects.create(user=request.user, type=NotoificationChoice.COMMENT)
        return redirect('home')


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "post/post_create.html"
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserPostListView(LoginRequiredMixin, TemplateView):

    template_name = 'posts.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        posts = Post.objects.filter(author=user)
        context["posts"]=posts
        return context

# class PostDetailView(LoginRequiredMixin, DetailView):
#     template_name = 'post/post_detail.html'
#     model = Post
#     context_object_name = "post"
