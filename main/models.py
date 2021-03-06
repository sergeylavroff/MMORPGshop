from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm
from django import forms
from ckeditor.fields import RichTextField


class UserNotif(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text='Заголовок объявления'
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Article(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        help_text='Заголовок объявления'
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    body = RichTextField(blank=True,null=True)


    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='article', )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.name}'
    def get_absolute_url(self):
        return f'/edit/{self.id}'

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    def __str__(self):
        return self.name


class Reply(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = RichTextField(blank=True,null=True)
    confirmed = models.BooleanField(default=False)
    def __str__(self):
        return ('По объявлению ' + self.article.name + ' от ' + self.user.email)
