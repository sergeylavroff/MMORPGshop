from django import forms
from django.db import models
from django.contrib import admin
from .models import Article, Category, Reply, UserNotif

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Reply)
admin.site.register(UserNotif)
