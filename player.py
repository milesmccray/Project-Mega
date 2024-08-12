from item import Item


class Player:
    """
    A class representing the "Player" object in the game.
    """
    def __init__(self, name='Default Joe'):
        self.name = name
        self.inventory = []
        self.current_room = None

    def add_item(self, item: Item):
        self.inventory.append(item)

    def remove_item(self, item: Item):
        self.inventory.remove(item)

    def update_room(self, room: str):
        self.current_room = room
