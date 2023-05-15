from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import Psychologist, Session, CommentUserPsychologist


class PsLoginForm(forms.Form):
    # username_field = 'email'
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control fc_1', 'placeholder': 'Enter email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control fc_2', 'placeholder': 'Enter secret key'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['container_class'] = 'form-group'
        self.fields['password'].widget.attrs['container_class'] = 'form-group'

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        try:
            user = Psychologist.objects.get(email=email)
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect email or password.')
        except Psychologist.DoesNotExist:
            raise forms.ValidationError('Incorrect email or password.')
        return cleaned_data


class RequestUpdateForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['is_confirmed']


class SessionUpdateForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['status']


class SignUpForSession(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date']


class CommentUserPsychologistForm(forms.ModelForm):
    class Meta:
        model = CommentUserPsychologist
        fields = ['comment_text', 'rating']




