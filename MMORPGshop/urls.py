"""MMORPGshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from main.views import ArticleList, ArticleCreateView, ArticleUpdateView, ReplyView, ArticleOne, ReplyList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ArticleList.as_view()),
    path('add', ArticleCreateView.as_view(), name='article_create'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='article_edit'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('more/<int:pk>/',ArticleOne.as_view(), name='article_one'),
    path('reply/<int:pk>/',ReplyView.as_view(success_url='/'), name='reply'),
    path('replies',ReplyList.as_view(), name='replies'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
