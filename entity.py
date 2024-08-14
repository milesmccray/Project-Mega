from item import Item
import pygame


class Entity:
    """
    A class representing an interactable entity or "container".
    Entities are located within room objects and can contain item objects
    """

    def __init__(self, name: str, description: str, position: list[float, float],
                 items: list[Item] = None, usable: bool = True):
        self.name = name                        # Game name of Entity object
        self.description = description          # Description of the Entity object
        self.position = pygame.Rect(position)   # [posX, posY, width, height] used for pygame.Rect # object
        self.items = items                      # List of items contained within the Entity object
        self.usable = usable                    # Determines if the Entity object is clickable by the player

    def update_description(self, description: str):
        self.description = description

    def remove_item(self, item):
        self.items.remove(item)

