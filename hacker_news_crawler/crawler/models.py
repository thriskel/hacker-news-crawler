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
