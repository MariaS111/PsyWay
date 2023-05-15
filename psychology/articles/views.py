from django.shortcuts import render, redirect
from .models import Article, CommentArticle
from .forms import ArticleForm, CommentArticleForm
from users.models import User
from psychologists.models import Psychologist
from django.urls import reverse
from django.db.models import Avg


def show_list(request):
    articles = Article.objects.all()
    # print(articles)
    context = {'articles': articles}
    return render(request, 'articles/list.html', context)


def article_list_by_date(request):
    articles = Article.objects.order_by('-publication_date')
    context = {'articles': articles}
    return render(request, 'article_list.html', context)


def article_list_by_rate(request):
    articles = Article.objects.annotate(avg_rating=Avg('commentuserpsychologist__rating')).order_by('-avg_rating')
    context = {'articles': articles}
    return render(request, 'article_list.html', context)


def article_view(request, pk):
    art = Article.objects.get(pk=pk)
    average_rating = CommentArticle.objects.filter(pk=pk).aggregate(Avg('rating'))[
        'rating__avg']
    context = {'article': art, 'avg_rate': average_rating}
    return render(request, 'articles/article.html', context)


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('profile')
    else:
        form = ArticleForm()

    context = {'form': form}
    return render(request, 'articles/create_article.html', context)


def comment_article_list(request, pk):
    comments = CommentArticle.objects.filter(article=pk)
    article = Article.objects.get(pk=pk)
    context = {'comments': comments, 'article': article}
    # article_comments_url = reverse('article_comments', kwargs={'pk': pk})
    return render(request, 'articles/comments.html', context)


def comment_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if isinstance(request.user, Psychologist):
                comment.psychologist = request.user
            elif isinstance(request.user, User):
                comment.user = request.user
            comment.article = article
            comment.save()
            article_url = reverse('article', kwargs={'pk': pk})
            return redirect(article_url)
    else:
        form = CommentArticleForm()
    context = {'form': form}
    return render(request, 'articles/create_comment.html', context)