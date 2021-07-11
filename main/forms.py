from django.forms import ModelForm
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArticleForm(ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Article
        fields = ['name', 'body', 'category']

class ReplySearch(ModelForm):
    article = forms.ModelChoiceField(queryset=Article.objects.all())
    class Meta:
        model = Reply
        fields = ['article']

class ReplyForm(ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Reply
        fields = ['text']

class ReplyAcceptForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['confirmed']