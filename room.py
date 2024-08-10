from entity import Entity
from item import Item


class Room:
    """
    A class representing the "room" in the game.
    Rooms can contain entity objects (which contain item objects) or item objects.
    """

    def __init__(self, description: str, image: str, entities: list[Entity] = None, items: list[Item] = None):
        self.description = description          # Description of Room object
        self.image = image                      # String containing path to image file
        self.entities = entities                # List of Entity objects contained within the room
        self.items = items                      # List of Item objects contained within the room

    def update_description(self, description: str):
        self.description = description

    def remove_entity(self, entity: Entity):
        self.entities.remove(entity)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def update_image(self, image: str):
        self.image = image
