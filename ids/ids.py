#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: awakenedhaki

"""
Parse Rosalind Bioinformatics Stronghold HTML table into list of problem IDs.
"""

import re
import json

from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import List

url_list_id = "http://rosalind.info/problems/list-view/"

def getHTML() -> str:
    """
    Return text from HTML table of Bioinformatics Stronghold.
    """
    r = urlopen(url_list_id)
    soup = BeautifulSoup(r, "html.parser")
    return soup.find("table", class_="problem-list").get_text()

def problemID(text: str) -> List[str]:
    """
    Return problem ids from Bioinformatics Stronghold problems.
    """
    pattern = re.compile("[A-Z]{2,4}")
    ids: List[str] = re.findall(pattern, text)
    return ids[1:]

def removeDups(list_: list) -> List[str]:
    """
    Remove duplicates of problem IDs list.
    """
    # no_dups is a list of elements without duplicates
    no_dups: List[str] = []
    for element in list_:
        if element not in no_dups:
            no_dups.append(element)
    return no_dups

def fetchProblemIDs() -> List[str]:
    """
    Fetch problem IDs from Bioinformatics Stronghold HTML table.
    """
    return removeDups(problemID(getHTML()))

def to_json(problem_ids: List[str]) -> None:
    """
    Save all problem IDs as a JSON file.
    """
    with open("ids.json", "w") as outfile:
        json.dump(problem_ids, outfile)

if __name__ == "__main__":
    to_json(fetchProblemIDs())