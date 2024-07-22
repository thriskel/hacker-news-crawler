from django.db import models
from django.core import validators


class Post(models.Model):
    rank = models.IntegerField(
        primary_key=True,
        validators=[
            validators.MaxValueValidator(30),
            validators.MinValueValidator(1)
        ]
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=150
    )
    title_length = models.IntegerField(
        validators=[
            validators.MinValueValidator(0)
        ]
    )
    score = models.IntegerField(
        validators=[
            validators.MinValueValidator(0)
        ]
    )
    comments = models.IntegerField(
        validators=[
            validators.MinValueValidator(0)
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def update_posts_details(cls, posts_details):
        """
        Creates or updates posts records
        """

        posts = []

        for post_detail in posts_details:
            try:
                post = cls.objects.get(rank=post_detail.rank)
            except cls.DoesNotExist:
                post = cls.objects.create(**post_detail.dict())
            else:
                for field, value in post_detail.dict().items():
                    if getattr(post, field) != value:
                        setattr(post, field, value)
                post.save()
            posts.append(post)

        return posts
