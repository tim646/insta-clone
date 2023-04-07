from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from apps.post.models import Post, Notification, Like, History
from apps.user.models import User


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        posts = Post.objects.all().exclude(author=self.request.user)
        suggestesion = User.objects.exclude(id=self.request.user.id).exclude(id__in=self.request.user.followings.all())
        histories = History.objects.order_by( 'author_id', '-created_at')
        ntcs = Notification.objects.filter(user=self.request.user, is_seen=False).count()
        context["posts"] = posts
        context["suggestion"] = suggestesion
        context["histories"] = histories
        context["ntcs"] = ntcs
        return context
