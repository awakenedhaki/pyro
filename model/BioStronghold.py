import os
import requests

from utils.utils import addNewLine
from bs4 import BeautifulSoup
from typing import List

home: str= os.getenv("HOME")

class BioStronghold:

    def __init__(self, id: str) -> None:
        self.id = id
        self.soup = None

    @property
    def dirPath(self) -> str:
        '''
        Sets the path to the new problem files directory
        '''
        return os.path.join(home, "rosalind", self.id.upper())

    @property
    def title(self) -> str:
        '''
        Sets the title of the README.md file
        '''
        self.soup.find("nobr").extract()
        return "# " + self.soup.find("h1").get_text().strip()

    @property
    def topic(self) -> str or None:
        '''
        Sets the topic of the given problem
        '''
        try:
            topic = self.soup.find("p", class_="topics").get_text()
            return " ".join(topic.split())
        except AttributeError:
            return None

    @property
    def sample(self) -> List[str]:
        '''
        Sets a list of sample dataset and output of given problem
        '''
        return list(map(lambda m: m.get_text(),
                        self.soup.find_all("div", class_="codehilite")))


    @property
    def statement(self) -> str:
        '''
        Sets the problem statement
        '''
        self.soup.find("blockquote").extract()
        prob = self.soup.find('div', class_='problem-statement').get_text().split()
        prob.remove("Problem")
        addNewLine(prob, 'Return:')
        addNewLine(prob, 'Dataset', sub=1)
        addNewLine(prob, 'Dataset', add_=1)
        addNewLine(prob, 'Output', sub=1)
        addNewLine(prob, 'Output', add_=1)
        return " ".join(prob)

    def scrape(self):
        '''
        Scrapes Rosalind for Bioinformatics Stronghold html content
        '''
        r = requests.get(f"http://rosalind.info/problems/{self.id}")
        self.soup = BeautifulSoup(r.content, "html.parser")
        return self

    def saveProblem(self) -> None:
        '''
        Saves statement, title, topics, and sample into problem directory
        '''
        self.makeDir()
        with open(self.dirPath + "/README.md", "w") as outfile:
            outfile.write(self.title + "\n\n")
            if self.topic is not None:
                outfile.write(self.topic + "\n\n")
            outfile.write(self.statement)
        with open(self.dirPath + "/sample.txt", "w") as data:
            data.write(self.sample[0])
        with open(self.dirPath + "/output.txt", "w") as output:
            output.write(self.sample[1])

    def makeDir(self) -> None:
        '''
        Creates problem directory if one does not exists
        '''
        if not os.path.exists(self.dirPath):
            os.mkdir(self.dirPath)

