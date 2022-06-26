from .models import *
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'choice_type',
            'post_to_category_rel',
            'create_date_time',
            'post_title',
            'post_text',
            'post_rating',
        ]
