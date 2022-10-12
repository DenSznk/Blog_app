from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.category_name


class Post(models.Model):
    NEWS = 'NE'
    ARTICLE = 'AR'
    POST_TAG = [
        (NEWS, 'News'),
        (ARTICLE, 'Article'),
    ]
    post_header = models.CharField(
        max_length=100,
        verbose_name='Header',
    )
    post_content = models.TextField(
        verbose_name='Content',
    )
    post_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='post_author_set',
        verbose_name='Author',
    )
    post_tag = models.CharField(
        max_length=2,
        choices=POST_TAG,
        default=NEWS,
    )
    post_date_added = models.DateTimeField(
        auto_now_add=True,
    )
    post_category = models.ManyToManyField(
        Category,
        through='PostCategory',
        verbose_name='Categories',
    )

    def get_preview(self):
        preview = f"{self.post_content[:50]}"
        if len(preview) > 50:
            preview += '...'
        return preview


class PostCategory(models.Model):
    post_id = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
