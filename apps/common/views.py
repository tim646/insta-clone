from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from apps.post.models import Post, Notification


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        posts = Post.objects.all()
        histories = []  # history
        notifications = Notification.objects.filter(user=request.user, is_seen=False)
        context = {
            "posts":posts,
            "histories":histories,
            "notifications":notifications
        }
        return render(request, "home.html", context=context)
