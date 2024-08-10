from item import Item


class Entity:
    """
    A class representing an interactable entity or "container".
    Entities are located within room objects and can contain item objects
    """

    def __init__(self, name: str, description: str, position: tuple[tuple[float, float], tuple[float, float]],
                 items: list[Item] = None, usable: bool = True):
        self.name = name                    # Unique name of the Entity object
        self.description = description      # Description of the Entity object
        self.position = position            # ((posX, posY), (width, height)) used for pygame.Rect object
        self.items = items                  # List of Item objects contained within the Entity object
        self.usable = usable                # Determines if the Entity object is clickable by the player

    def update_description(self, description: str):
        self.description = description

    def remove_item(self, item):
        self.items.remove(item)
