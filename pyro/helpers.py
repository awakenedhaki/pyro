import json

from pathlib import Path
from click import echo
from operator import itemgetter
from blessings import Terminal
from typing import Callable, Dict

ROSALIND = Path.home() / '.rosalind'

EXTENSIONS = {'python': 'py'}

TERMINAL = Terminal()


def format_(*problems, complete=False):
    values: Callable = itemgetter('id', 'title', 'solved_by', 'correct_ratio')
    for problem in problems:
        id_, title, solved_by, correct_ratio = values(problem)
        problem_text = f'%-4s {TERMINAL.bright_blue("-->")} %-59s (%-16s - %s)'

        solved_by = TERMINAL.bright_green(solved_by)
        correct_ratio = TERMINAL.bold_green(correct_ratio)

        if complete:
            details = itemgetter('given', 'return', 'sample_dataset',
                                 'sample_output')
            given, return_, sample_dataset, sample_output = details(problem)
            problem_text += '\n\nGiven: %s\nReturn: %s\n\nSample Dataset: %s\n\nSample Output: %s'
            echo(problem_text % (id_, title, solved_by, correct_ratio, given,
                                 return_, sample_dataset, sample_output))
        else:
            echo(problem_text % (id_, title, solved_by, correct_ratio))


def find_by_id(problems, id, details=False, return_problem=False):
    for i, problem in enumerate(problems['data']):
        if problem['id'] == id.upper():
            format_(problem, complete=details)
            if return_problem:
                return problem
            break
        elif i == len(problems['data']) - 1:
            raise ValueError(f'Problem ID {id} does not exists.')


def find_by_index(problems, index, details=False, return_problem=False):
    if index < 0:
        raise ValueError(
            f'Problem index must be a positive number, not {index}')

    try:
        problem = problems['data'][index]
        format_(problem, complete=details)
        if return_problem:
            return problem
    except (IndexError, TypeError):
        raise ValueError(
            f'Problem index must be greater than 0, and less than {problems["num_problems"]}'
        )


def touch(language: str, problem: Dict[str, str]):
    language = language.lower()
    if not ROSALIND.exists():
        raise AssertionError(
            'Must run the setup command before using any other functionality.')

    if language in EXTENSIONS:
        LANGUAGES_JSON = Path(__file__) / 'jsons' / 'languages.json'
        with open(LANGUAGES_JSON, 'r') as f:
            template_path = eval(json.load(f)[language])
            with open(template_path, 'r') as f:
                template = f.read()

        values = itemgetter('title', 'given', 'return', 'sample_dataset',
                            'sample_output')
        filepath = ROSALIND / f'{problem["id"]}.{EXTENSIONS[language]}'
        with open(filepath, 'w') as f:
            f.write(template % values(problem))
