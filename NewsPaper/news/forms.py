from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    post_title = forms.CharField(min_length=20)
    # post_text = forms.TextInput

    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_to_category_rel',
            'post_text',
            'author',
        ]

    def clean(self):
        cleaned_data = super().clean()
        post_text = cleaned_data.get('post_text')
        if post_text is not None and len(post_text) < 50:
            raise ValidationError({
                "post_text": "Текст не может быть меньше 50 символов."
            })
        return cleaned_data
