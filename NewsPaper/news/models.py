from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        sum_Post = 0
        sum_Comment = 0
        post_Rating = self.post_set.all().aggregate(postRating=Sum('rating'))
        sum_Post += post_Rating.get('postRating')

        comment_Rating = self.author.comment_set.all().aggregate(commentRating=Sum('rating'))

        sum_Comment += comment_Rating.get('commentRating')

        self.ratingAuthor = sum_Post * 3 + sum_Comment
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLES = 'AR'

    CATEGORY_OF_POST = (
        (NEWS, 'Новости'),
        (ARTICLES, 'Статьи'),
    )

    category_Type = models.CharField(max_length=2, choices=CATEGORY_OF_POST, default=ARTICLES)
    date_Creation = models.DateTimeField(auto_now_add=True)
    post_Category = models.ManyToManyField(Category, through='Post_Category')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:124] + '...'

class Post_Category(models.Model):
    post_Key = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_Key = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_User = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_Of_Create = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
