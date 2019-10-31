class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"Item: {self.name}\nDescription: {self.current_room.name}"

    def __repr__(self):
        return f"Item: {repr(self.name)}\nDescription: {repr(self.current_room.name)}"