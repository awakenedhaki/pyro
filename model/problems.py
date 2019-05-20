from collections.abc import Mapping

class Problems(Mapping):

    def __init__(self, problems):
        self.problems = problems

    def __getitem__(self, key):
        key_ = self.find_key(key)
        return self.problems[key_]

    def __len__(self):
        return len(self.problems)

    def __iter__(self):
        return self.problems.items()

    def find_key(self, key):
        key_ = next(
            (dict_key for dict_key in self.problems.keys() if key in dict_key),
            None
        )
        if not key_:
            raise KeyError(key)
        return key_
