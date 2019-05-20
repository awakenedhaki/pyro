import json

from dataclasses import is_dataclass, asdict


class EnhancedJSONEncoder(json.JSONEncoder):
    """
    EnhancedJSONEncoder extends the json.JSONEncoder to allow for proper serialization of dataclasses.dataclass object.
    """

    def default(self, o: object):
        """
        Overriding the default method in the json.JSONEncoder class.

        keyword arguments:
            o -- A python object
        """
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)
