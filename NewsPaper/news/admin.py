from django.contrib import admin
from .models import Author, Category, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date_time', 'post_title', 'post_to_category_rel', 'author', 'choice_type')
    list_filter = ('post_to_category_rel', 'author', 'choice_type')
    search_fields = ('post_title', 'post_text')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date_time', 'comment_text', )
    list_filter = ('create_date_time', )
    search_fields = ('comment_text', )


# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
