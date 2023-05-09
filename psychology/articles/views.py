from django.shortcuts import render, redirect
from .models import Article


def show_list(request):
    articles = Article.objects.all()
    # print(articles)
    context = {'articles': articles}
    return render(request, 'articles/list.html', context)


def article_view(request, pk):
    art = Article.objects.get(pk=pk)
    context = {'article': art}
    return render(request, 'articles/article.html', context)