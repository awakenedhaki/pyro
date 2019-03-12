from model.TupledKeyDict import TupledKeyDict

__author__ = "awakenedhaki"

import click

from persistence.ProblemsJSON import ProblemsJSON

@click.command()
@click.option("-n", "--next")
@click.option("-s", "--select")
@click.option("-c", "--check")
@click.option("-l", "--list", is_flag=True)
def main(next, select, check, list):
    problems = ProblemsJSON().unferment()
    pass

if __name__ == '__main__':
    main()
