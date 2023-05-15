from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, default='articles/article.png')
    file = models.FileField(upload_to='articles/documents/', blank=True)
    authors = models.ManyToManyField('psychologists.Psychologist')
    publication_date = models.DateTimeField(auto_now_add=True)
    section = models.ManyToManyField('Section')

    def __str__(self):
        return self.title


class Section(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return self.topic


class CommentArticle(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    psychologist = models.ForeignKey('psychologists.Psychologist', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    comment_text = models.TextField()
    rating = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ])

    def __str__(self):
        return f"{self.comment_text} {self.rating}"
