from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from .models import Post, Category, Author
from .filters import PostFilter
from .forms import PostForm, UserForm
from datetime import date


# Create your views here.
def index(request):
    return render(request, 'index.html')


class PostsList(ListView):
    model = Post
    ordering = '-create_date_time'
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post_detail'


class PostSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'search_post'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreateNews(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today_news_count'] = len(Post.objects.filter(
            author=self.request.user.author,
            create_date_time__date=date.today())
        ) >= 3
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_type = 'NW'
        post.author = self.request.user.author
        data = form.data
        email(data)
        return super().form_valid(form)


def email(data):
    recipients = []
    category = Category.objects.get(pk=data['post_to_category_rel'])
    for i in category.subscribers.all():
        if i.email == "":
            continue
        else:
            recipients.append([i.email, i.username])
    for i, j in recipients:
        html_content = render_to_string(
            'new_post_email.html', {
                "data": data, "recipient": j, }
        )
        email_i = [i]
        msg = EmailMultiAlternatives(
            subject=f'Новый пост: {data["post_title"]}',
            body=data["post_text"],
            from_email='django_test12345@sobago.ru',
            to=email_i,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()


class PostCreateArticle(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post',)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_type = 'AR'
        post.author = self.request.user.author
        data = form.data
        email(data)
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.change_post',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    permission_required = ('news.delete_post',)


class ProfileDetail(DetailView):
    model = User
    template_name = 'profile_detail.html'
    context_object_name = 'profile_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    model = User
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('post_list')


@login_required
def get_author(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
        Author.objects.create(author_user=user)
    return redirect('/')


class CategoryList(ListView):
    model = Category
    ordering = 'cat_name'
    template_name = 'categorys_subscribe.html'
    context_object_name = 'categorys'
    paginate_by = 10


@login_required
def get_subscribe(request, pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    category.subscribers.add(user)
    return redirect('/categorys/')


@login_required
def del_subscribe(request, pk):
    user = request.user
    category = Category.objects.get(pk=pk)
    category.subscribers.remove(user)
    return redirect('/categorys/')
