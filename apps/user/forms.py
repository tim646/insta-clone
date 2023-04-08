from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, User

from allauth.account.forms import SignupForm
from captcha.fields import ReCaptchaField

from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': 'Password'}))
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        captcha_response = cleaned_data.get('captcha')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password', code='invalid_login')
        if not captcha_response:
            raise forms.ValidationError('Error verifying reCAPTCHA, please try again', code='invalid_captcha')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password', 'captcha')


class EditProfileForm(forms.ModelForm):
    user_image = forms.ImageField(required=False)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}))
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Bio'}))
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'URL'}))
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}))

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'bio', 'url', 'location']

    def save(self, commit=True):
        user_profile = super().save(commit=False)
        user_profile.image = self.cleaned_data['user_image']
        if commit:
            user_profile.save()
            user_profile.user.save()
        return user_profile


class UserRegisterForm(UserCreationForm, SignupForm):
    username = forms.CharField(
       widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}), max_length=55, required=True)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'First Name'}), max_length=60, required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Last Name'}), max_length=60, required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}), required=True)

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
