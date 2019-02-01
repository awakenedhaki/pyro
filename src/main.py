#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: awakenedhaki

'''
Rosalind Bioinformatics Stronghold web scraper. Given a problem ID, a
README.md file is created with the contents of the specified problems.

The README.md is created within a directory named after the problem ID.
'''

import click
import utils.suggest

from urllib.error import HTTPError
from utils.misc import vMessage, markComplete
from pyro import pyro

@click.command(help='''Creates a Markdown file for a given Rosalind 
               Bioinformatics Stronghold problem ID.''')
@click.option('-p', '--problem', default=None,
              help='Requested problem.')
@click.option('-v', '--verbose', is_flag=True,
              help='Print more information.')
@click.option('-c', '--complete', default=None, type=str,
              help='Marks directories as complete')
def main(problem, verbose, complete):
    '''
    '''
    try:
        if id is not None:
            pyro(problem)
        if complete is not None:
            markComplete(complete)
        if verbose:
            vMessage(language, problem)
    except HTTPError:
        suggest.suggestCorrection(problem)

if __name__ == '__main__':
    main()
