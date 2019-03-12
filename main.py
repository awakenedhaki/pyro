#! /usr/bin/env python

__author__ = "awakenedhaki"

import os
import json
import click

from model.Problem import Problem
from model.TupledKeyDict import TupledKeyDict
from persistence.ProblemsJSON import ProblemsJSON

with open("config.json", "r") as infile:
    config = json.load(infile)

home = os.getenv("HOME")
path = os.path.join(home, config["path"])

@click.command()
@click.option("-p", "--problem", help="Problem ID or index")
@click.option("-l", "--language", default="python",
              help="Programming language for template")
@click.option("--listed", is_flag=True)
@click.option("-v", "--verbose", is_flag=True)
def main(problem, language, listed, verbose):
    problems: TupledKeyDict = ProblemsJSON().unferment()
    if problem:
        Problem().setUp(problems[problem],
                        path,
                        config["templates"][language])
    if listed:
        pass

if __name__ == '__main__':
    main()
