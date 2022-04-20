from django.contrib import admin
from django.urls import path
from .views import index, PostsList, PostDetail, PostSearch, PostCreateNews, PostCreateArticle, PostUpdate, PostDelete, \
    ProfileUpdate, ProfileDetail, get_author

urlpatterns = [
    path('index', index),
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view(), name='post_search'),
    path('news/create/', PostCreateNews.as_view(), name='news_create'),
    path('articles/create/', PostCreateArticle.as_view(), name='articles_create'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('user/<int:pk>/edit/', ProfileUpdate.as_view(), name='user_edit'),
    path('user/<int:pk>/', ProfileDetail.as_view(), name='user_profile'),
    path('upgrade/', get_author, name='upgrade'),
]
