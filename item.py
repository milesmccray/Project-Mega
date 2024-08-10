class Item:
    """
    A class representing item object in the game.
    Items are found in room or entity objects. Can also be associated with player object (inventory)
    """

    def __init__(self, name: str, description: str, position: tuple[tuple[float, float], tuple[float, float]] = None,
                 usable: bool = True):
        self.name = name                        # Unique name for Item object
        self.description = description          # Description of the Item object
        self.position = position                # Only used for Item objects found outside of Entity objects
        self.usable = usable                    # Determines if the Item is clickable by the player

