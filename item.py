import pygame


class Item:
    """
    A class representing item object in the game.
    Items are found in room or entity objects. Can also be associated with player object (inventory)
    """

    def __init__(self, name: str, description: str, position: list[float, float] = None,
                 entity: bool = None, usable: bool = True):
        self.name = name  # Game name of the Item Object
        self.description = description  # Description of the Item object

        # Checks if item object has a room position
        if position:
            self.position = pygame.Rect(position)
        else:
            self.position = position

        self.entity = entity  # Indicates what Entity the Item is found in
        self.usable = usable  # Determines if the Item is clickable by the player

    def update_description(self, description: str):
        self.description = description
