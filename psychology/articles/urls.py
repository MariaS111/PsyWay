from django.urls import path
from .views import show_list, article_view, create_article, comment_article, comment_article_list, article_list_by_date, article_list_by_rate
from django.urls import re_path

urlpatterns = [
    path('', show_list, name='list_of_articles'),
    path('rate/', article_list_by_rate, name='article_by_rate'),
    path('date/', article_list_by_date, name='article_by_date'),
    path('<int:pk>/', article_view, name='article'),
    path('create/', create_article, name='create_article'),
    path('<int:pk>/comments/', comment_article_list, name='article_comments'),
    path('<int:pk>/comments/add_comment/', comment_article, name='article_comment'),
]