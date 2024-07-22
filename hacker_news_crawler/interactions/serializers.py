from . import models as interactions_models
from rest_framework import serializers


class InteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = interactions_models.Interaction
        fields = [
            'requested_at',
            'filters_used',
        ]
