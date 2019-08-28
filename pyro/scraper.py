import re
import json
import requests

from functools import partial
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString
from typing import List, Generator, Dict, Callable, Union

ROSALIND = 'http://rosalind.info/problems/'
STRONGHOLD: str = 'http://rosalind.info/problems/list-view/'


def fetch(url: str) -> BeautifulSoup:
    with requests.get(url) as response:
        return BeautifulSoup(response.content, 'html.parser')


def parse_stronghold(soup: BeautifulSoup
                     ) -> Generator[Dict[str, str], None, None]:
    def problem_info(row: Tag) -> Dict[str, str]:
        '''
        Split row into corresponding variables:
            - id: Problem ID (str)
            - title: Problem title (str)
            - solved_by: Number of people who have solved the problem (str)
            - correct_ratio: Perecentage attempts that are correct (str)

        Keyword Arguments:
            - row: An HTML tr element, representing a table row
        '''
        tds: List[Tag] = row.find_all('td')
        id, title, solved_by, _ = [td.get_text().strip() for td in tds]
        correct_ratio = re.match(r'width: (\d+%);',
                                 tds[-1].div.div['style']).group(1)

        return {
            'id': id,
            'title': title,
            'solved_by': solved_by,
            'correct_ratio': correct_ratio
        }

    def problem_details(id_: str) -> Dict[str, str]:
        '''
        Returns a problem's:
            - Given: Parameters of a problem.
            - Return: Expected output
            - Sample Dataset: Example input
            - Sample Output: Example output

        Keyword Argument:
            - id_: Problem ID
        '''
        soup: BeautifulSoup = fetch(ROSALIND + id_)
        remove_special: Callable[[str], str] = partial(
            re.compile(r'\$|Given: |Return: ').sub, '')

        given, return_ = \
            [remove_special(param.parent.get_text().strip())
             for param in soup.find_all(class_='given-return')]
        sample_dataset, sample_output = \
            [sample.get_text().strip()
             for sample in soup.find_all(class_='codehilite')[-2:]]

        return {
            'given': given,
            'return': return_,
            'sample_dataset': sample_dataset,
            'sample_output': sample_output
        }

    tbody: Tag = soup.find('tbody').find_all('tr')
    for row in tbody:
        p_info: Dict[str, str] = problem_info(row)
        yield {**p_info, **problem_details(p_info['id'])}


if __name__ == "__main__":
    soup: BeautifulSoup = fetch(STRONGHOLD)
    problems: List[Dict[str, str]] = list(parse_stronghold(soup))
    data: Dict[str, Union[List[Dict[str, str]], int, str]] = {
        'data': problems,
        'num_problems': len(problems),
        'url': ROSALIND
    }
    with open('problems.json', 'w') as f:
        json.dump(data, f)
