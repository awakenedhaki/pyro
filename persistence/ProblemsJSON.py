import json
from typing import Dict

from model.TupledKeyDict import TupledKeyDict

class ProblemsJSON():

    def ferment(self, problems: TupledKeyDict) -> None:
        """
        Saves list of Problem as a JSON object.
        :param problems:
        :return: None
        """
        with open("./problems.json", "w") as outfile:
            # Convert key to string, JSON cannot store tuple
            json.dump({str(k): v for k, v in problems.items()}, outfile)

    def unferment(self) -> TupledKeyDict:
        with open("./problems.json", "r") as infile:
            dictLoad: Dict = json.load(infile)
        return TupledKeyDict().from_dict(dictLoad)
