from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, User


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control fc_1', 'placeholder': 'Enter username', 'container': 'div'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control fc_2', 'placeholder': 'Enter password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['container_class'] = 'form-group'
        self.fields['password'].widget.attrs['container_class'] = 'form-group'


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control fc_3', 'placeholder': 'Enter username', 'container': 'div'}))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control fc_4', 'placeholder': 'Enter first name', 'container': 'div'}))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control fc_5', 'placeholder': 'Enter last name', 'container': 'div'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control fc_6', 'placeholder': 'Enter email', 'container': 'div'}))
    inf = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control fc_7 ', 'placeholder': 'Enter some information about you', 'container': 'div'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control fc_8', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control fc_9', 'placeholder': 'Enter password again'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'inf', 'password1', 'password2']


# class UserUpdateForm(forms.ModelForm):
#     inf = forms.CharField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'inf']
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'first_name', 'last_name', 'email', 'inf']