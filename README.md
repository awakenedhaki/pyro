# Pyro

Pyro is a command-line tool implemented in Python 3 that scrapes problem statements from the Rosalind Project Bioinformatics Stronhold.

If you want to check out the Rosalind Project, click on this [link](http://rosalind.info/problems/list-view/).

As of yet, this tool is not fully developed. 

You can create an `pyro` alias in your .aliases, .bashrc, .bash_profile, .zshrc, etc, which points towards `main.py` file in `~/Pyro` directory.

To get started create a file in your home directory called Rosalind.

```bash
mkdir ~/Rosalind
```

In order to request a problem statement, you must write the following into your terminal.

```bash
pyro -p dna
```

You can also specify the problem by number.

```bash
pyro -p 1
```

Either action will gather problem statement, sample data, and sample output and write them into files within a new directory. The directory will be named as `001 - DNA`. 

Further development will focus on checking whether your script output, when running against the sample data, is the same as the sample output provided. Another feature would be creating template files for your specified languages.

__TODO__:

* Check if script output matches sample output
* Create templates files in specified languages
* Fix suggest.py
