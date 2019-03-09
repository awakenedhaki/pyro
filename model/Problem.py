class Problem():

    soup = None

    def __init__(self, num, id) -> None:
        self.num = num
        self.id = id
        self.title = None
        self.body = None
        self.data = None
        self.output = None
        self.topics = None

    def to_dict(self):
        """
        Dictionary representation of Problem object,
        containing the object's fields.
        :return: dict
        """
        return self.__dict__
