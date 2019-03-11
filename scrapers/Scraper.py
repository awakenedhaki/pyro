import requests

from bs4 import BeautifulSoup
from requests import Response
from typing import Dict


class Scraper():

    """
    Abstract class of Scraper that is not meant for instantiation.
    """

    url = None
    params: Dict = {}

    def scrape(self):
        """
        Scrape HTML from rosalind given parameters (params) and a url.
        Converts and parses scraped HTML using BeautifulSoup.
        :return: self
        """
        r: Response = requests.get(self.url, params=Scraper.params, timeout=5)
        r.close() # Close connection
        self.soup = BeautifulSoup(r.content, "html.parser").body
        return self