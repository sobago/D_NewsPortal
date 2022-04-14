import django.forms
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post, Author


class PostFilter(FilterSet):
    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Любой'
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

