from django.contrib import admin
from django.urls import path
from .views import index, PostsList, PostDetail

urlpatterns = [
    path('index', index),
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
