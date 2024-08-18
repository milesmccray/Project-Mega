import pygame


class Item:
    """
    A class representing item object in the game.
    Items are found in room or entity objects. Can also be associated with player object (inventory)
    """

    def __init__(self, name: str, description: str, position: list[float, float], events: dict[callable, bool]):

        self.name = name                # Game name of the Item Object
        self.description = description  # Description of the Item Object
        # Checks if item object has position value
        if position:
            self.position = pygame.Rect(position)
        else:
            self.position = position

        self.events = events            # Dict of possible events associated with Item Object

    def update_description(self, description: str):
        self.description = description
