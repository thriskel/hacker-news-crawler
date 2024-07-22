from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class CrawlerTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.interactions_url = '/interactions/'

    def test_list(self):
        response = self.client.get(self.interactions_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
