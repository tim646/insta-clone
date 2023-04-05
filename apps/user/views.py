from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import ListView
from .models import User, Saved
# Create your views here.
from ..post.models import Post, PostMedia


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        # call the parent form_valid method to save the form
        valid = super().form_valid(form)
        # get the username and password
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        # authenticate user then login
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, 'Account created successfully')
        return valid

    def form_invalid(self, form):
        messages.error(self.request, 'Error creating account')
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True


class SavedPostView(LoginRequiredMixin, ListView):
    template_name = 'saved.html'

    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs.get('username'))
        saved = Saved.objects.filter(user=self.user)
        return saved

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(object_list=object_list, **kwargs)
        followers_count = self.user.followers.count()
        following_count = self.user.followings.count()
        post_count = self.user.posts.count()
        context['followers_count'] = followers_count
        context['followings_count']= following_count
        context['post_count']= post_count
        return context


def profile(request):

    user = User.objects.get(username=request.user.username)
    followers_count = user.followers.count()  # get the number of followers for user
    following_count  = user.followings.count()
    user_posts = Post.objects.filter(author=user)
    post_count = user_posts.count()
    context = {'user': user, 'followers_count': followers_count, 'followings_count': following_count,
               'post_count': post_count, 'user_posts': user_posts}
    return render(request, 'myprofile.html', context)


@login_required
def follow(request, pk):
    if request.method == 'POST':
        user = request.user
        user_to_follow = User.objects.get(pk=pk)
        request.user.userprofile.follow(user_to_follow)
        return redirect('profile', pk=pk)
    return redirect('home')


@login_required
def unfollow(request, pk):
    if request.method == 'POST':
        user = request.user
        user_to_unfollow = User.objects.get(pk=pk)
        request.user.userprofile.follow(user_to_unfollow)
        return redirect('profile', pk=pk)
    return redirect('home')
