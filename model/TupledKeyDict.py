from click import Tuple


class TupledKeyDict(dict):

    """
    TupledKeyDict extends dict(), allowing for the N keys for 1 value.

    Methods being overriden:
        self.__getitems__

    New methods:
        self.specifiedKeys
    """

    def __init__(self):
        super()

    def __getitem__(self, key) -> Tuple:
        """
        Accepts a single value, and iteratively check if the value is within
        a key tuple of the dictionary.
        :param key: object
        :return: object
        """
        for keyTuple in self.keys():
            if key in keyTuple:
                return self.get(keyTuple)

    def specifiedKeys(self, index) -> Tuple:
        """
        Returns a tuple of keys, from a specified index
            keys = (("key1_0", "key1_1),
                    ("key2_0", "key2_1))
            self.specifiedKeys(1) -> ("key1_1", "key2_1")
        :param index: int
        :return: Tuple[object]
        """
        return tuple(zip(*self.keys()))[index]

    def __repr__(self):
        return str(self)
