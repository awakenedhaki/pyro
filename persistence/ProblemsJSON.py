import json

from model.TupledKeyDict import TupledKeyDict

class ProblemsJSON():

    def ferment(self, problems: TupledKeyDict) -> None:
        """
        Saves list of Problem as a JSON object.
        :param problems:
        :return: None
        """
        with open("./rosalindProblems/problems.json", "w") as outfile:
            json.dump({str(k): v for k, v in problems.items()}, outfile)

    def unferment(self) -> TupledKeyDict:
        with open("./rosalindProblems/problems.json", "r") as infile:
            dictLoad = json.load(infile)
        return TupledKeyDict().from_dict(dictLoad)
