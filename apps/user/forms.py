from django import forms
from .models import UserProfile, User

from django.contrib.auth.forms import UserCreationForm


class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'full Name'}), required=True)
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'URL'}), required=True)
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}), required=True)

    class Meta:
        model = UserProfile
        fields = ['image', 'full_name', 'bio', 'url', 'location']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
       widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}), max_length=55, required=True)
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': ''}), max_length=55, required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), required=True)

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2']
