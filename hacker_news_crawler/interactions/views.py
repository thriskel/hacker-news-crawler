from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models as interactions_models
from . import serializers as interactions_serializers


class Interaction(APIView):
    """
    View to return interactions with the crawler API
    """

    def get(self, request):
        """
        Returns a list of interactions
        """

        interactions = interactions_models.Interaction.objects.all().order_by(
            '-created_at'
        )

        serializer = interactions_serializers.InteractionsSerializer(
            interactions,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
