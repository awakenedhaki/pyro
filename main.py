#! /usr/bin/env python

# author: awakenedhaki

import click

from model.BioStronghold import BioStronghold

@click.command()
@click.option("--id")
def main(id: str):
    BioStronghold(id).scrape().saveProblem()

if __name__ == "__main__":
    main()