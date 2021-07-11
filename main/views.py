from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article, Reply
from .forms import ArticleForm, ReplyForm, ReplyAcceptForm, ReplySearch
from .filters import ReplyFilter


class ArticleList(ListView):
    model = Article
    template_name = 'main.html'
    context_object_name = 'articles'
    ordering = ['-creation_date']

class ReplyList(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'replies.html'
    context_object_name = 'replies'
    def get_queryset(self, **kwargs):
        replies = Reply.objects.filter(article__author__exact=self.request.user)
        form = ReplySearch(self.request.GET)
        if form.is_valid():
            article_form = form.cleaned_data['article']
            replies = replies.filter(article = article_form)
        return replies
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplySearch(self.request.GET)
        return context

class ArticleOne(DetailView):
    model = Article
    template_name = 'article_one.html'
    context_object_name = 'art'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_add.html'
    form_class = ArticleForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article_delete.html'
    context_object_name = 'article'
    success_url = '/'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        if Article.objects.get(pk=id).author == self.request.user:
            return Article.objects.get(pk=id)
        else:
            raise PermissionError

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article_add.html'
    form_class = ArticleForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        if Article.objects.get(pk=id).author == self.request.user:
            return Article.objects.get(pk=id)
        else:
            raise PermissionError


class ReplyView(LoginRequiredMixin, CreateView):
    template_name = 'reply_add.html'
    form_class = ReplyForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        id = self.kwargs.get('pk')
        form.instance.article = Article.objects.get(pk=id)
        return super().form_valid(form)

class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'reply_delete.html'
    context_object_name = 'reply'
    success_url = '/'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        if Reply.objects.get(pk=id).article.author == self.request.user:
            return Reply.objects.get(pk=id)
        else:
            raise PermissionError

class ReplyAcceptView(LoginRequiredMixin, UpdateView):
    template_name = 'reply_accept.html'
    context_object_name = 'reply'
    success_url = '/replies'
    form_class = ReplyAcceptForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        if Reply.objects.get(pk=id).article.author == self.request.user:
            return Reply.objects.get(pk=id)
        else:
            raise PermissionError