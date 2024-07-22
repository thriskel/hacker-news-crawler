from datetime import datetime

from django.db import models


class Interaction(models.Model):
    requested_at = models.DateTimeField(
        verbose_name='Requested at'
    )
    filters_used = models.JSONField(
        verbose_name='Filters used'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def create_interaction(cls, filters):
        filters_used = {
            'title_length_gt': None,
            'title_length_lt': None
        }

        title_length_gt = filters.get('title_length_gt')
        title_length_lt = filters.get('title_length_lt')

        if title_length_gt:
            filters_used.update(
                {'title_length_gt': title_length_gt}
            )
        if title_length_lt:
            filters_used.update(
                {'title_length_lt': title_length_lt}
            )

        cls.objects.create(
            requested_at=datetime.now(),
            filters_used=filters_used
        )
