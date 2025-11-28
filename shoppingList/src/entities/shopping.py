"""Shopping entity module."""


class Shopping:
    """Represents a shopping item. """

    def __init__(self, id_, name, amount, owner):
        self.id = id_
        self.name = name
        self.amount = amount
        self.owner = owner


    @classmethod
    def from_dict(cls, data):
        return cls(data.get("id"), data.get("name"), data.get("amount"), data.get("owner"))
