# parsers.py

from bs4 import BeautifulSoup
from typing import List
from misc import addNewLine

def parseHeader(html: BeautifulSoup) -> str:
    '''
    Obtain header from problem site.
    '''
    header: str = html.find('h1')
    unwanted = html.find('nobr')
    unwanted.extract()
    return header.get_text().strip()

def parseProblem(html: BeautifulSoup) -> str:
    '''
    Obtain problem statement, and separate components with newlines.
    '''
    problem: str = html.find('div', class_='problem-statement')
    unwanted = html.find('blockquote')
    unwanted.extract()
    parsing: List[str] = problem.get_text().split()
    addNewLine(parsing, 'Return:')
    addNewLine(parsing, 'Dataset', sub=1)
    addNewLine(parsing, 'Dataset', add_=1)
    addNewLine(parsing, 'Output', sub=1)
    addNewLine(parsing, 'Output', add_=1)
    if 'Note' in parsing:
        addNewLine(parsing, 'Note')
    parsing.remove('Problem')
    return ' '.join(parsing)

def parseTopic(html: BeautifulSoup) -> str or None:
    '''
    Obtain problem topic as string, otherwise return None.
    '''
    try:
        topic: str = html.find('p', class_='topics').get_text()
        parsed_topic: str = ' '.join(topic.split()[1:])
        return parsed_topic
    except AttributeError:
        return None

def parseSample(html: BeautifulSoup) -> List[str]:
    '''
    Obtain a list of sample data and output.
    '''
    matches = map((lambda m: m.get_text()), html.find_all('div', class_='codehilite'))
    filtered = list(filter((lambda s: not s.startswith('http://')), matches))
    return filtered

