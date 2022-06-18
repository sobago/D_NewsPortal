from .models import Post, Category
from modeltranslation.translator import register, TranslationOptions


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('post_title', 'post_text')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('cat_name', )
