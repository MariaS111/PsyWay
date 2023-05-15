from django import forms
from .models import Article, Section
from articles.models import CommentArticle


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control fc_3', 'placeholder': 'Enter title', 'container': 'div'}))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control fc_4', 'placeholder': 'Enter content', 'container': 'div'}))
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control fc_5', 'container': 'div', 'label': 'Choose file'}))
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control fc_6', 'container': 'div', 'label': 'Choose file'}))

    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'file', 'authors', 'section']
        widgets = {
            'authors': forms.SelectMultiple(attrs={'class': 'form-control fc_7', 'placeholder': 'Choose authors'}),
            'section': forms.SelectMultiple(attrs={'class': 'form-control fc_8', 'placeholder': 'Choose sections'}),
        }


class CommentArticleForm(forms.ModelForm):
    class Meta:
        model = CommentArticle
        fields = ['comment_text', 'rating']