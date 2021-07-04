from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text='Заголовок объявления'
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    body = models.CharField(max_length=1024, help_text='Описание объявления')

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='article', )
    author = models.ManyToManyField(User)

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    def __str__(self):
        return self.name


class Reply(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
