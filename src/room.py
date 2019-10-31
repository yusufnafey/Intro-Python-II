# Implement a class to hold room information. This should have name and description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def add_items(*args):
        for i in args:
            self.items.append(i)
    
    def __str__(self):
        return f"Room: {self.name}\nDescription: {self.description}\nRoom Items: {self.items}"

    def __repr__(self):
        return f"Room: {repr(self.name)}\nDescription: {repr(self.description)}\nRoom Items: {repr(self.items)}"