from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class CrawlerTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.news_url = '/news/'
        self.valid_filters = {'title_length_gt': 5,
                              'title_length_lt': 5}

    def test_list(self):
        response = self.client.get(self.news_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data[0]

        rank = data['rank']
        title = data['title']
        title_length = data['title_length']
        score = data['score']
        comments = data['comments']

        self.assertIsInstance(rank, int)
        self.assertIsInstance(title, str)
        self.assertIsInstance(title_length, int)
        self.assertIsInstance(score, int)
        self.assertIsInstance(comments, int)
