from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserRegisterForm, UserLoginForm, EditProfileForm
from django.views.generic import CreateView, DetailView, TemplateView
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import ListView
from .models import User, Saved, UserProfile
# Create your views here.
from ..post.models import Post, PostMedia, History


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
    model = Saved
    context_object_name = 'saved'
    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs.get('username'))
        saved = Saved.objects.filter(user=self.user)
        return saved

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(object_list=object_list, **kwargs)
        followers_count = self.user.profile.followers.count()
        followings_count = self.user.followings.count()
        post_count = self.user.posts.count()
        context['followers_count'] = followers_count
        context['followings_count']= followings_count
        context['post_count']= post_count
        return context


class UserDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        posts = Post.objects.filter(author=user)
        followers_count = user.followers.count()
        following_count = user.followings.count()
        history = History.objects.filter(author = user)
        context['user'] = user
        context['followers_count'] = followers_count
        context['followings_count'] = following_count
        context["posts"] = posts
        context["histories"] = history
        return context


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'myprofile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username=self.request.user.username)
        followers_count = user.followers.count()
        followings_count = user.followings.count() # get the number of followers for user

        posts = Post.objects.filter(author=user)
        post_count = posts.count()
        context['user'] = user
        context['followers_count'] = followers_count
        context['followings_count'] = followings_count
        context['post_count'] = post_count
        context['user_posts'] = posts
        return context


@login_required
def follow(request, pk):
    if request.method == 'POST':
        user = UserProfile.objects.get(user_id=request.user.id)
        user_to_follow = User.objects.get(pk=pk)
        print(user_to_follow)
        user.follow(user_to_follow)
        return redirect('profile')
    return redirect('home')


@login_required
def unfollow(request, pk):
    if request.method == 'POST':
        user = UserProfile.objects.get(user_id=request.user.id)
        user_to_follow = User.objects.get(pk=pk)
        print(user_to_follow)
        user.unfollow(user_to_follow)
        return redirect('profile')
    return redirect('home')




def edit_profile(request):
    user_profile = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})
