# misc.py

import os
import json

from typing import List

def load_problemID() -> List[str]:
    '''
    Load problem ID json file.
    '''
    home: str = os.getenv('HOME')
    pyro_path = f'{home}/pyro/ids'
    with open(f'{pyro_path}/ids.json', 'r') as infile:
        ids: List[str] = json.load(infile)
    return ids

def addNewLine(list_: List[str], str_, sub = 0, add_ = 0) -> List[str]:
    '''
    Insert two two \n at str_ index or str_ index - sub + add.
    '''
    index: int = list_.index(str_) - sub + add_
    list_.insert(index, '\n\n')
    return list_

def vMessage(lang: str, id: str):
    '''
    TODO: Provide description of actions taking place
    '''
    pass

def markComplete(problem: str) -> None:
    '''
    '''
    os.rename(problem, f'{problem.upper()}_done')

