from item import Item
import pygame


class Entity:
    """
    A class representing an interactable entity or "container".
    Entities are located within room objects and can contain item objects
    """

    def __init__(self, name: str, description: str, group: int, position: list[float, float], usable: bool = True):
        self.name = name                        # Game name of Entity object
        self.description = description          # Description of the Entity object
        self.group = group                      # 1 = Door | 2 = "Container"
        self.position = pygame.Rect(position)   # [posX, posY, width, height] used for pygame.Rect # object
        self.usable = usable                    # Determines if the Entity object is clickable by the player
        self.items = []                         # List of Item objects contained within the Entity object

    def update_description(self, description: str):
        self.description = description

    def remove_item(self, item: Item):
        self.items.remove(item)

    def add_item(self, item: Item):
        self.items.append(item)

