#! /usr/bin/env python

# author: awakenedhaki

import click

from model.BioStronghold import BioStronghold

@click.command()
@click.option("--id")
@click.option("-v", "--verbose", is_flag=True)
def main(id, verbose):
    p = BioStronghold(id)
    if id:
        p.scrape().saveProblem()
    if verbose:
        p.verbose()

if __name__ == "__main__":
    main()