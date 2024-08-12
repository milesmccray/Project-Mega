class Item:
    """
    A class representing item object in the game.
    Items are found in room or entity objects. Can also be associated with player object (inventory)
    """

    def __init__(self, description: str, position: tuple[tuple[float, float], tuple[float, float]] = None,
                 entity: bool = None, usable: bool = True):
        self.description = description  # Description of the Item object
        self.position = position  # Only used for Item objects found outside of Entity objects
        self.entity = entity  # Indicates what Entity the Item is found in
        self.usable = usable  # Determines if the Item is clickable by the player

    def update_description(self, description: str):
        self.description = description
