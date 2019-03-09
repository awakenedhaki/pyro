from scrapers.Scraper import Scraper

class ProblemScraper(Scraper):

    """
    Scrapes a problem from Rosalind Bioinformatics Stronghold.
    """

    def __init__(self, id):
        Scraper.url = "http://rosalind.info/problems/" + id
        Scraper.params = {}
