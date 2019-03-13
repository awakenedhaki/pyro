import os

from typing import List

def printColumns(keys: List[str]) -> None:
    """
    Prints problem IDS in columns.
    TODO: Fix alignment and equal spacing
    :param keys: List[str]
    :return: None
    """
    columns = []
    inter = []
    for key in keys:
        if len(inter) >= 10:
            columns.append(inter)
            inter = []
        else:
            inter.append(key)
    columns.append(inter)
    for element in zip(*columns):
        print("\t".join(element))

