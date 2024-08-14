import json
from item import Item
from entity import Entity


class Bedroom:
    def __init__(self):
        self.name = 'Bedroom'
        self.description = 'Your childhood bedroom'
        self.image = 'data/rooms/bedroom_demo.png'
        self.entities = None
        self.items = None

        with open('data/object_data.json', 'r') as f:
            object_data = json.load(f)

        ####################### DECLARE ITEM OBJECTS #########################
        br_helmet = Item(**object_data['items']['br_helmet'])
        br_doorkey = Item(**object_data['items']['br_doorkey'])
        br_chestkey = Item(**object_data['items']['br_chestkey'])

        ####################### DECLARE ENTITY OBJECTS #######################
        br_bed = Entity(**object_data['entities']['br_bed'])
        br_chest = Entity(**object_data['entities']['br_chest'])

        ####################### BUILD ROOM ###################################
        self.entities = [br_bed, br_chest]
        self.items = [br_helmet, br_doorkey, br_chestkey]

    def remove_entity(self, entity: Entity):
        self.entities.remove(entity)

    def remove_item(self, item: Item):
        self.items.remove(item)

