from typing import List
from scrapers.Scraper import Scraper

class IdListScraper(Scraper):

    def __init__(self, location=None):
        Scraper.params["location"] = location
        Scraper.url = "http://rosalind.info/problems/list-view/"

    @property
    def ids(self) -> List[str]:
        """
        IDs of Rosalind Bioinformatics Stronghold problems
        :return: List[str]
        """
        return [tr.td.get_text()
                for tr in self.soup.find("tbody").find_all("tr")]
