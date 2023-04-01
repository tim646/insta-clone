from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.


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




    # def get_success_url(self):
    #     return reverse_lazy('tasks')