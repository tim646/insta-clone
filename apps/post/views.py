from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, TemplateView, ListView

from apps.post.choices import NotoificationChoice
from apps.post.forms import PostCreateForm, PostMediaFormSet, HistoryCreateForm
from apps.post.models import Post, Like, Notification, Comment, History
from apps.user.models import User, Saved


class PressLikeView(View, LoginRequiredMixin):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
        if created and not Notification.objects.filter(user=post.author, type=NotoificationChoice.LIKE).exists():
            Notification.objects.create(user=request.user, type=NotoificationChoice.LIKE)

        return redirect('home')


class CommentCreateView(View, LoginRequiredMixin):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        Comment.objects.create(post=post.id, body=request.POST['comment'], author=self.request.user)
        Notification.objects.create(user=post.author, type=NotoificationChoice.COMMENT)
        return redirect('home')


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    context_object_name = 'notifications'
    template_name = 'notifations.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(object_list=object_list, **kwargs)
        for notification in context['notifications']:
            notification.is_seen=True
            notification.save()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['post_media_formset'] = PostMediaFormSet(self.request.POST, self.request.FILES)
        else:
            context['post_media_formset'] = PostMediaFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        post_media_formset = context['post_media_formset']
        if post_media_formset.is_valid():
            self.object = form.save(commit=False)
            self.object.author = self.request.user
            self.object.save()
            post_media_formset.instance = self.object
            post_media_formset.save()
            return redirect('profile')
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UserPostListView(LoginRequiredMixin, TemplateView):
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        posts = Post.objects.filter(author=user)
        context["posts"] = posts
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    queryset = Post.objects.all()
    template_name = 'post/post_detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostSaveView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        saved, created = Saved.objects.get_or_create(user=request.user, post=post)
        if not created:
            saved.delete()
        return redirect('home')


class HistoryCeateView(CreateView):
    model = History
    template_name = 'history_create.html'
    form_class = HistoryCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HistoryDetailView(DetailView):
    model = History
    template_name = 'history_detail.html'
    context_object_name = 'history'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.mark_seen(self.request.user)
        return obj
