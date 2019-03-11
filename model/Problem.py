from typing import Dict

class Problem():

    """
    Problem is a Rosalind Bioinformatics Stronhold Problem object
    """

    soup = None

    def __init__(self, num=None, id=None) -> None:
        self.num = num
        self.id = id
        self.title = None
        self.body = None
        self.data = None
        self.output = None
        self.topics = None

    def to_dict(self) -> Dict:
        """
        Dictionary of Problem instance variables.
        :return: dict
        """
        classDict = {"className": self.__class__,
                     "moduleName": self.__module__}
        classDict.update(self.__dict__)
        return classDict
