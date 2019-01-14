# pyro.py

import os
import json
import parsers

from urllib.request import urlopen
from bs4 import BeautifulSoup
from typing import List
from misc import load_problemID

home: str = os.getenv('HOME')
path = f'{home}/rosalind'

pyro_path = f'{home}/pyro'

url = 'http://rosalind.info/problems'

def fetchProblem(id: str) -> str:
    '''
    Return Bioinformatics Stronghold specified problem ID description.
    '''
    r = urlopen(f'{url}/{id}')
    soup = BeautifulSoup(r, 'html.parser')
    header: str = parsers.parseHeader(soup)
    topics: str or None = parsers.parseTopic(soup)
    problem: str = parsers.parseProblem(soup)
    dataset, output = parsers.parseSample(soup)
    return (header, topics, problem, dataset, output)

def idNum(id: str) -> int:
    '''
    Position of id in ids.json list
    '''
    with open(f'{pyro_path}/ids/ids.json', 'r') as infile:
        pos: List[int] = json.load(infile)
    return pos.index(id) + 1

def makeSample(sample: str, id: str, type: str) -> None:
    '''
    Make a sample .txt file in problem ID directory.
    '''
    with open(f'{type}_{id}.txt', 'w') as outfile:
        outfile.write(sample)

def makeREADME(header: str, topics: str, problem: str) -> None:
    '''
    Make a sample .txt file in problem ID directory.
    '''
    with open('README.md', 'w') as outfile:
        outfile.write(f'## {header}\n\n')
        if topics is None:
            outfile.write('No listed topics.\n\n')
        else:
            outfile.write(f'Topics: {topics}\n\n')
        outfile.write(f'{problem}')

def pyro(id: str or int) -> None:
    '''
    Writes README.md, dataset and output files for given problem id.
    '''
    if id.isdigit():
        for i, prob in enumerate(load_problemID()):
            if str(i + 1) == id:
                id = prob
    header, topics, problem, dataset, output = fetchProblem(id)
    id = id.upper()
    id_num: int = idNum(id)
    try:
        os.chdir(f'{path}/{id_num:0>3} - {id}')
    except FileNotFoundError:
        os.mkdir(f'{path}/{id_num:0>3} - {id}')
        os.chdir(f'{path}/{id_num:0>3} - {id}')
    finally:
        makeSample(dataset, id, 'dataset')
        makeSample(output, id, 'output')
        makeREADME(header, topics, problem)
