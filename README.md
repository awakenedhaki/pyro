# Pyro: Python Rosalind, Bioinformatics Stronghold

Pyro is a command-line interface for the Rosalind Project's Bioinformatics Stronghold Platform. You will be able to access a variety of bioinformatics problems through this CLI.

Take note that the problems were __not__ written by me. All problems are hosted in the [Rosalind's Team website](http://rosalind.info).

## Set Up

To get started, you can clone this repo. You can then add the following line to your aliases dotfile.

```bash
alias pyro=[...]
```

Where the brackets hold the path to the `main.py` file in this repo.

To get started, you must first create a directory called `rosalind` in your home directory. You can use the following command to create the rosalind directory.

```bash
mkdir ~/rosalind
```

You can also select your preferred location for the rosalind directory by changing the `config.json` file. You will want to write the path, not including your home directory.

For example, if you want the path to be `~/github/rosalind`. You would change the `path` field in the json file, and set it to `github/rosalind`.

## Manual

To select a problem, you can request it by ID, in lower or upper case.

```bash
pyro --problem dna
```

You can also specify a problem through index.

```bash
pyro --problem 1
```

If you want to also create a template file for your solution, you can include the `--language` option.

```bash
pyro --problem dna --language java
```

The language option is set to python by default. At the moment, there are only templates for python, java, and R.
