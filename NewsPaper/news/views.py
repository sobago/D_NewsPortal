from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'index.html')


class PostsList(ListView):
    model = Post
    ordering = 'post_text'
    template_name = 'news.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post_detail'
