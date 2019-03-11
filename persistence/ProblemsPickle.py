import pickle

from model.TupledKeyDict import TupledKeyDict

class ProblemsPickle():

    def ferment(self, problems: TupledKeyDict) -> None:
        """
        Saves list of Problem as a JSON object.
        :param problems:
        :return: None
        """
        with open("./rosalindProblems/problems.pickle", "wb") as outfile:
            pickle.dump(problems, outfile)

    def unferment(self) -> TupledKeyDict:
        with open("./rosalindProblems/problems.pickle", "rb") as infile:
            problems = pickle.load(infile)
        return problems

