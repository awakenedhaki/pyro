import re
import requests

from bs4 import BeautifulSoup, SoupStrainer

from .cloaking import headers_rand_user_agent, delay
from parsers.problem_parser import ProblemParser

class ProblemScraper(object):

    url: str = "http://rosalind.info"
    
    def scrape(self, path, tag=None, return_url=False):
        headers = headers_rand_user_agent()
        r = requests.get(self.url + path, 
                         headers=headers)
        r.close()
        # delay()
        if return_url:
            return [BeautifulSoup(r.content, 
                                 "html.parser", 
                                 parse_only=SoupStrainer(tag)),
                    r.url]
        return BeautifulSoup(r.content, 
                             "html.parser", 
                             parse_only=SoupStrainer(tag))

    def run(self):
        soup = self.scrape(path="/problems/list-view/", tag="tbody")
        hrefs = [row["href"] for row in soup.find_all("a")][0::2]
        for href in hrefs:
            yield self.problem(href)

    def problem(self, href):
        soup, url = self.scrape(path=href, return_url=True)
        for tag in soup(["blockquote", "table", "nobr"]):
            tag.decompose()
        return ProblemParser.parse(soup, url)
