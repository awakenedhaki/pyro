from typing import List

def addNewLine(list_: List[str], str_, sub=0, add_=0) -> List[str]:
    '''
    Insert two two \n at str_ index or str_ index - sub + add.
    '''
    index: int = list_.index(str_) - sub + add_
    list_.insert(index, '\n\n')
    return list_
