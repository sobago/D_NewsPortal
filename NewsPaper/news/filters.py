import django.forms
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post, Author, Category


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Любой'
    )

    post_to_category_rel = ModelChoiceFilter(
        field_name='post_to_category_rel',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Любая'
    )

    create_date_time = DateFilter(
        lookup_expr='gt',
        label='Начальная дата',
        widget=django.forms.DateInput(
            attrs={'type': 'date'}
        ),
    )

    class Meta:
        model = Post
        fields = {
            'post_title': ['icontains'],
        }

