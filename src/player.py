# Write a class to hold player information, e.g. what room they are in currently.

class Player:
    def __init__(self, name, current_room, current_inventory=[]):
        self.name = name
        self.current_room = current_room
        self.current_inventory = current_inventory

    def get_item(self, item):
        self.current_room.items.remove(item)
        self.current_inventory.append(item)

    def drop_item(self, item):
        self.current_room.items.append(item)
        self.current_inventory.remove(item)

    def __str__(self):
        return f"Player Name: {self.name}\nCurrent Room: {self.current_room.name}\nCurrent Inventory: {self.current_inventory}"

    def __repr__(self):
        return f"Player Name: {repr(self.name)}\nCurrent Room: {repr(self.current_room.name)}\nCurrent Inventory: {repr(self.current_inventory)}"