from django.contrib import admin
from django.urls import path
from .views import index, PostsList, PostDetail, PostSearch, PostCreateNews, PostCreateArticle, PostUpdate, PostDelete

urlpatterns = [
    path('index', index),
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view(), name='post_search'),
    path('news/create/', PostCreateNews.as_view(), name='news_create'),
    path('articles/create/', PostCreateArticle.as_view(), name='articles_create'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
]
