__author__ = "awakenedhaki"

import json
import click

from parsers.ProblemJSONParser import ProblemJSONParser

@click.command()
def main():
    with open("rosalindProblems/problems.json", "r") as infile:
        problems = json.load(infile)

if __name__ == '__main__':
    main()