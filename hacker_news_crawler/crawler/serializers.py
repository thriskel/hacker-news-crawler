from . import models as crawler_models
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = crawler_models.Post
        fields = [
            'rank',
            'title',
            'title_length',
            'score',
            'comments'
        ]
