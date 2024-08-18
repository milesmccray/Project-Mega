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
        br_door = Entity(**object_data['entities']['br_door'])

        ####################### ADD ITEM OBJECTS TO ENTITY OBJECTS ###########
        br_bed.add_item(br_chestkey)
        br_chest.add_item(br_doorkey)

        ####################### BUILD ROOM ###################################
        self.entities = [br_bed, br_chest, br_door]  # All entity objects in the room
        self.items = [br_helmet]                     # All item objects in the room

    def remove_entity(self, entity: Entity):
        self.entities.remove(entity)

    def remove_item(self, item: Item):
        self.items.remove(item)

x = Bedroom()