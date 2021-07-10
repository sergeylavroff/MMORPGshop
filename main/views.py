from django.http import HttpRequest
from django.views.generic import ListView, UpdateView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Article, Reply
from .forms import ArticleForm, ReplyForm


class ArticleList(ListView):
    model = Article
    template_name = 'main.html'
    context_object_name = 'articles'
    ordering = ['-creation_date']

class ReplyList(ListView):
    model = Reply
    template_name = 'replies.html'
    context_object_name = 'replies'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Reply.objects.filter(article__author_id=id)



class ArticleOne(ListView):
    model = Article
    template_name = 'article_one.html'
    context_object_name = 'article'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_add.html'
    form_class = ArticleForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'article_add.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)


class ReplyView(CreateView):
    template_name = 'reply_add.html'
    form_class = ReplyForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        id = self.kwargs.get('pk')
        form.instance.article = Article.objects.get(pk=id)
        return super().form_valid(form)