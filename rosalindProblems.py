import time

from model.Problem import Problem
from parsers.ProblemHTMLParser import ProblemHTMLParser
from scrapers.IdListScraper import IdListScraper
from scrapers.ProblemScraper import ProblemScraper
from persistence.ProblemsJSON import ProblemsJSON

def rosalindProblems() -> None:
    """
    Scrape data of all Rosalind Bioinformatics Stronghold problems.
    Stores scraped data as JSON.
    :return: None
    """
    problems = []
    ids = IdListScraper("bioinformatics-stronghold").scrape().ids
    probHTMLParser = ProblemHTMLParser()
    size = len(ids)
    progress = 0
    for num, id in enumerate(ids):
        pSoup = ProblemScraper(id).scrape().soup
        problems.append(probHTMLParser\
                        .parseHTML(pSoup, Problem(num + 1, id)).to_dict())
        time.sleep(3)
        progress += 1
        # Percentage progress
        print(str(round(progress/size * 100, 1)) + "%", flush=True, end="\r")
    ProblemsJSON().to_json(problems)

if __name__ == '__main__':
    rosalindProblems()
