from dataclasses import dataclass
from typing import List

@dataclass
class Problem(object):
    id: str
    title: str
    statement: str
    given: str
    return_: str
    input_: str
    output: str
    topics: List[str] or None = None
