from django.forms import ModelForm
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArticleForm(ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Article
        fields = ['name', 'body', 'category']

class ReplyForm(ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Reply
        fields = ['text']

    # def save(self, commit=True):
    #     self.instance.user = self.request.user
    #     return super().save(commit=commit)