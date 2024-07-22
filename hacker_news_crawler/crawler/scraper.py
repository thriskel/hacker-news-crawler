import requests

from bs4 import BeautifulSoup as bs

from . import schemas as crawler_schemas
from . import exceptions as crawler_exceptions
from . import utils as hnc_utils


class HRScraper:
    """
    Scraps the information from the top 30
    posts from hacker rank
    """

    def __init__(self, url):
        try:
            response = requests.get(url)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.MissingSchema
        ):
            raise crawler_exceptions.ServiceUnavailable()
        self.soup = bs(response.text, 'html.parser')

    def get_posts_data(self) -> list[tuple]:
        """
        Extracts both parts of a post information
        """

        # Find all classed tr elements
        classed_rows = self.soup.find_all('tr', class_='athing')

        # Combine classed and unclassed rows into pairs
        combined_objects = []
        for row in classed_rows:
            next_row = row.next_sibling
            combined_objects.append((row, next_row))

        return combined_objects

    def scrape_details(self) -> list[crawler_schemas.PostUpdate]:
        """
        Obtains the details from HR posts data.
        """

        posts_data = self.get_posts_data()

        data = []

        for title_row, info_row in posts_data:
            row_data = {}

            # extract rank and title from title row
            title_data = title_row.find_all('td', class_='title')

            rank = title_data[0].find('span', class_='rank')
            if not rank:
                continue
            rank = int(rank.text.strip('.'))
            title = title_data[1].find(
                'span',
                class_='titleline'
            ).find('a').text.strip()

            # extract score and comments from info row
            info_data = info_row.find(
                'td',
                class_='subtext'
            ).find('span', class_='subline')

            score = 0
            comments = 0
            if info_data:
                score = info_data.find(
                    'span',
                    class_='score'
                ).text.strip()
                score = int(score.split(' ')[0]) if score else 0
                comments = info_data.find(
                    string=lambda text: text and text.endswith("comments")
                )
                comments = int(comments.split('\xa0')[0]) if comments else 0

            # set data and append it to the list
            row_data = crawler_schemas.PostUpdate(
                rank=rank,
                title=title,
                title_length=hnc_utils.get_title_length(title),
                score=score,
                comments=comments
            )

            data.append(row_data)

        return data
