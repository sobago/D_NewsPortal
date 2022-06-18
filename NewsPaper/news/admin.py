from django.contrib import admin
from .models import Author, Category, Post, Comment
from modeltranslation.admin import TranslationAdmin


class PostAdminTrans(TranslationAdmin):
    model = Post


class CategoryAdminTrans(TranslationAdmin):
    model = Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name', )
    list_filter = ('cat_name', )
    search_fields = ('cat_name', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date_time', 'post_title', 'post_to_category_rel', 'author', 'choice_type')
    list_filter = ('post_to_category_rel', 'author', 'choice_type')
    search_fields = ('post_title', 'post_text')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date_time', 'comment_text', )
    list_filter = ('create_date_time', )
    search_fields = ('comment_text', )


# Register your models here
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
