from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя автора')
    author_rating = models.IntegerField(default=0, verbose_name='Рейтинг автора')

    def update_rating(self):
        post_rat = self.post_set.aggregate(postRating=Sum('post_rating'))
        pRat = 0
        pRat += post_rat.get('postRating')

        comment_rat = self.author_user.comment_set.aggregate(commentRating=Sum('comment_rating'))
        cRat = 0
        cRat += comment_rat.get('commentRating')

        self.author_rating = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return self.author_user.username

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    cat_name = models.CharField(max_length=128, unique=True, verbose_name='Название категории')

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')

    NEWS = 'NW'
    ARTICLE = 'AR'
    TYPE_CHOICES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    ]

    choice_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=ARTICLE, verbose_name='Тип статьи')
    create_date_time = models.DateTimeField(auto_now_add=True)
    post_to_category_rel = models.ManyToManyField(Category, through='PostCategory', verbose_name='Категория')
    post_title = models.CharField(max_length=254, verbose_name='Название статьи')
    post_text = models.TextField(verbose_name='Текст статьи')
    post_rating = models.IntegerField(default=0, verbose_name='Рейтинг статьи')

    def post_preview(self):
        return f'{self.post_text[:123]}...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def __str__(self):
        return f'{self.post_title} : {self.post_text}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostCategory(models.Model):
    post_rel = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_rel = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_to_post_rel = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Статья')
    comment_to_user_rel = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    comment_text = models.TextField(verbose_name='Текст комментария')
    create_date_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0, verbose_name='Рейтинг комментария')

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
