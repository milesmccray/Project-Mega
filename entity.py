from item import Item
import pygame


class Entity:
    """
    A class representing an interactable entity or "container".
    Entities are located within room objects and can contain item objects
    """

    def __init__(self, name: str, description: str, events: dict[callable, bool], position: list[float, float]):
        self.name = name                        # Game name of Entity object
        self.description = description          # Description of the Entity object
        self.events = events                    # Dict of possible events associated with Entity Object
        self.position = pygame.Rect(position)   # [posX, posY, width, height] used for pygame.Rect # object
        self.items = []                         # List for Item objects contained within the Entity object

    def update_description(self, description: str):
        self.description = description

    def remove_item(self, item: Item):
        self.items.remove(item)

    def add_item(self, item: Item):
        self.items.append(item)

