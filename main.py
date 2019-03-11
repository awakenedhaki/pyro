__author__ = "awakenedhaki"

import click

from persistence.ProblemsPickle import ProblemsPickle

@click.command()
def main():
    problems = ProblemsPickle().unferment()

if __name__ == '__main__':
    main()
