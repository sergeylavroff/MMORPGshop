from django import forms
from django.contrib import admin
from .models import Article, Category, Reply

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Reply)
