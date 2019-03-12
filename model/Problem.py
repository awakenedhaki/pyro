import os
import shutil

from typing import Dict

class Problem():

    """
    Problem is a Rosalind Bioinformatics Stronhold Problem object
    """

    def __init__(self, num=None, id=None) -> None:
        self.num = num
        self.id = id
        self.title = None
        self.body = None
        self.data = None
        self.output = None
        self.topics = None

    @property
    def dirName(self):
        return f"{self.num}_{self.id}"

    def from_dict(self, otherProblem):
        """
        Sets a dictionary with Problem fields to __dict__
        :param otherProblem: dict
        :return: Problem
        """
        self.__dict__ = otherProblem
        return self

    def to_dict(self) -> Dict:
        """
        Dictionary of Problem instance variables.
        :return: dict
        """
        classDict = {"className": self.__class__.__name__,
                     "moduleName": self.__module__}
        classDict.update(self.__dict__)
        return classDict

    def setUp(self, otherProblem, path, lang) -> None:
        """

        :param otherProblem: Dict
        :return: None
        """
        self.__dict__ = otherProblem
        self.createDocuments(path, lang)

    def createDocuments(self, path, lang) -> None:
        """

        :return: None
        """
        with open(f"./languageTemplates/template.{lang}", "r") as infile:
            template = infile.read()
        try:
            os.chdir(path)
            os.mkdir(self.dirName)
        except FileNotFoundError as e:
            raise Exception("Missing rosalind directory at home.")
        except FileExistsError as e:
            pass
        finally:
            dest = os.path.join(path, self.dirName, f"solution.{lang}")
            print(str(dest))
            with open(dest, "w") as outfile:
                outfile.write(template)