from django.contrib import admin
from articles.models import Article, Section, CommentArticle

admin.site.register(Article)
admin.site.register(Section)
admin.site.register(CommentArticle)
