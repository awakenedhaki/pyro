#! /usr/bin/env python

__author__ = "awakenedhaki"

import os
import json
import click

from utils import printColumns
from model.Problem import Problem
from model.TupledKeyDict import TupledKeyDict
from persistence.ProblemsJSON import ProblemsJSON

with open("config.json", "r") as infile:
    config = json.load(infile)

home = os.getenv("HOME")
path = os.path.join(home, config["path"])

@click.command(help="Command-line interface for Rosalind Bioinformatics Stronghold Problems.")
@click.option("-p", "--problem", help="Problem ID or index")
@click.option("-l", "--language", default="python",
              help="Programming language for template")
@click.option("--listids", is_flag=True)
@click.option("--check", is_flag=True)
@click.option("-v", "--verbose", is_flag=True)
def main(problem, language, listids, check, verbose):
    problems: TupledKeyDict = ProblemsJSON().unferment()
    if problem:
        Problem().setUp(problems[problem.upper()],
                        path,
                        config["templates"][language])
    if listids:
        keys = map(lambda e: " - ".join(e), problems.keys())
        printColumns(keys)
    if check:
        pass
    if verbose:
        pass

if __name__ == '__main__':
    main()
