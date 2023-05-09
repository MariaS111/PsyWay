from django.urls import path
from .views import show_list, article_view

urlpatterns = [
    path('', show_list, name='list_of_articles'),
    path('<int:pk>/', article_view, name='article'),
]