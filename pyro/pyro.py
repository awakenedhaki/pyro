import json
import click

from helpers import find_by_id, find_by_index, touch, format_
from subprocess import Popen, PIPE
from pathlib import Path
from typing import Union

PROBLEMS = Path.cwd() / 'jsons' / 'problems.json'
with open(PROBLEMS, 'r') as f:
    problems = json.load(f)


@click.group()
def main():
    pass


@main.command()
def setup():
    rosalind = Path.home() / '.rosalind/'
    click.echo(f'Creating .rosalind/ directory at {rosalind}')
    try:
        rosalind.mkdir()
    except FileExistsError:
        click.echo(
            f'{rosalind} already exists. You can keep that current directory, or delete and re-run this command.'
        )


@main.command()
@click.option('--id', default=None, type=str)
@click.option('--index', default=None, type=int)
@click.option('-d', '--details', is_flag=True)
@click.option('-l', '--language')
def show(id: str, index: int, details: bool, language: str):
    if index is not None:
        problem = find_by_index(problems, index, details, return_problem=True)
    elif id is not None:
        problem = find_by_id(problems, id, details, return_problem=True)
    else:
        if language:
            raise AssertionError(
                'The -l/--language option can only be specified if --id or --index is declared.'
            )
        format_(*problems['data'])

    if language is not None:
        touch(language, problem)


@main.command()
@click.argument('filename', nargs=1)
def test(filename: str):
    filepath = Path.home() / '.rosalind' / filename
    with Popen(['python3', filepath], stdout=PIPE) as process:
        stdout, _ = process.communicate()

    stdout = stdout.decode('utf-8').strip()
    click.echo(f'Output: {stdout}')


if __name__ == "__main__":
    main()
