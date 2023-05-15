from django import forms
from .models import Chat
from psychologists.models import Psychologist


class ChatForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control fc_3', 'placeholder': 'Enter name', 'container': 'div'}))
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control fc_4', 'placeholder': 'Enter description', 'container': 'div'}))
    is_private = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control fc_5', 'container': 'div', 'data-attr': 'Is private'}), label='Private')

    class Meta:
        model = Chat
        fields = ['name', 'description', 'is_private', 'psychologists', 'users']
        widgets = {
            'psychologists': forms.SelectMultiple(attrs={'class': 'form-control fc_6', 'placeholder': 'Choose psychologists'}),
            'users': forms.SelectMultiple(attrs={'class': 'form-control fc_7', 'placeholder': 'Choose users'}),
        }