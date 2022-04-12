from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from pprint import pprint


# Create your views here.
def index(request):
    return render(request, 'index.html')


class PostsList(ListView):
    model = Post
    ordering = '-create_date_time'
    template_name = 'news.html'
    context_object_name = 'posts'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     pprint(context)
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post_detail'
