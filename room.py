
class Room:
    def __init__(self, description: str, locations: list, image: str, entities: list = None, items: list = None):
        self.description = description  # String containing description of the room
        self.locations = locations  # List of strings of connecting rooms
        self.image = image  # String containing path to image file
        self.entities = entities  # List of class entities that can be interacted with in the room
        self.items = items  # List of class items that can be found in the room

    def update_description(self, description: str):
        self.description = description

    def remove_object(self, entity):
        self.entities.remove(entity)

    def update_image(self, image: str):
        self.image = image
