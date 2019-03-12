import time
from typing import List

from model.Problem import Problem
from model.TupledKeyDict import TupledKeyDict
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
    problems: TupledKeyDict[dict] = TupledKeyDict()
    ids: List[str] = IdListScraper("bioinformatics-stronghold").scrape().ids
    probHTMLParser = ProblemHTMLParser()
    size = len(ids)
    progress = 0
    for num, probID in enumerate(ids):
        pSoup = ProblemScraper(probID).scrape().soup
        problems[(str(num + 1), probID)] = (probHTMLParser \
                                            .parseHTML(pSoup, Problem(num + 1, probID)).to_dict())
        time.sleep(3)
        progress += 1
        # Percentage progress
        print(f"{num}: {probID} - {str(round(progress/size * 100, 2))}%",
              flush=True, end="\r")
    ProblemsJSON().ferment(problems)

if __name__ == '__main__':
    rosalindProblems()
