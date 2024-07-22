from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .scraper import HRScraper
from . import models as crawler_models
from . import serializers as crawler_serializers


class Crawler(APIView):
    """
    View to return Hacker rank data
    """

    def filter_post(self, queryset, query_params):
        """
        filters queryset based on title length filters
        """

        title_length_gt = query_params.get('title_length_gt')
        title_length_lt = query_params.get('title_length_lt')

        if title_length_gt:
            queryset = queryset.filter(title_length__gt=title_length_gt)
        if title_length_lt:
            queryset = queryset.filter(title_length__lt=title_length_lt)

        return queryset.order_by('rank')

    def get(self, request):
        """
        Scraps Hacker rank data, updates it if needed
        and returns it as a json.
        """

        url = getattr(settings, 'HACKER_RANK_NEWS_URL')

        scraper = HRScraper(url)

        posts_details = scraper.scrape_details()

        crawler_models.Post.update_posts_details(
            posts_details
        )

        queryset = self.filter_post(
            crawler_models.Post.objects.all(),
            request.query_params
        )

        serializer = crawler_serializers.PostSerializer(
            queryset,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
