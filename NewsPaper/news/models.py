from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rat = self.post_set.aggregate(postRating=Sum('post_rating'))
        pRat = 0
        pRat += post_rat.get('postRating')

        comment_rat = self.author_user.comment_set.aggregate(commentRating=Sum('comment_rating'))
        cRat = 0
        cRat += comment_rat.get('commentRating')

        self.author_rating = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    cat_name = models.CharField(max_length=128, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    TYPE_CHOICES = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    ]

    choice_type = models.CharField(max_length=2, choices=TYPE_CHOICES, default=ARTICLE)
    create_date_time = models.DateTimeField(auto_now_add=True)
    post_to_category_rel = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=254)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def post_preview(self):
        return f'{self.post_text[:123]}...'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()


class PostCategory(models.Model):
    post_rel = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_rel = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_to_post_rel = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_to_user_rel = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date_time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
