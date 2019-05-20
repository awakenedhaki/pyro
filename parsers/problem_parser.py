from bs4 import BeautifulSoup
from typing import List
from model.problem import Problem

class ProblemParser(object):

    @staticmethod
    def parse(problem_soup: BeautifulSoup, url: str):
        id: str = url.split("/")[-2]
        title: str = problem_soup.h1.text.strip()
        try:
            topics: List[str] or None = [topic.text 
                                         for topic in problem_soup.find("p", {"class": "topics"}).find_all("a")]
        except AttributeError:
            topics = None
        input_, output = [i.text 
                          for i in problem_soup.find_all("div", {"class": "codehilite"})][-2:]
        css_selector = "problem-statement problem-statement-bordered"
        paragraphs = [p.text.strip()
                      for p in problem_soup.find("div", {"class": f"{css_selector}"}).find_all("p")]
        return_: str = paragraphs.pop()
        given: str = paragraphs.pop()
        statement: str = " ".join(paragraphs).replace("\n", " ")
        return Problem(id, title, statement,
                       given, return_, input_, output, topics)
