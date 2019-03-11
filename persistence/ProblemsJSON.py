import json

from typing import List
from model.Problem import Problem

class ProblemsJSON():

    def to_json(self, problems: List[Problem]) -> None:
        """
        Saves list of Problem as a JSON object.
        :param problems:
        :return: None
        """
        with open("./rosalindProblems/problems.json", "w") as outfile:
            json.dump(problems, outfile)
