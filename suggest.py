# suggest.py

import os
import json

from typing import List
from misc import load_problemID

def suggestCorrection(id: str) -> None:
    '''
    TODO: Review
    If HTTPError, provide possible correct ID spelling options to user.
    '''
    problem_ids: List[str] = load_problemID()
    input_id: List[str] = sorted(list(id))
    for id in problem_ids:
        if input_id == sorted(list(id)):
            new_id: str = input(f'\nDid you mean {id}? [y/n] ')
            if new_id == 'y':
                pyro(id)
                break
    else:
        print('\nID not found.')

