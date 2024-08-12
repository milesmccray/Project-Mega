"""Unpacks the JSON file into objects"""
import json
from item import Item
from entity import Entity
from room import Room


# Open JSON File
with open('data/object_data.json', 'r') as f:
    object_data = json.load(f)

####################### DECLARE ITEM OBJECTS #######################
# Bedroom
br_helmet = Item(**object_data['items']['br_helmet'])
br_doorkey = Item(**object_data['items']['br_doorkey'])
br_chestkey = Item(**object_data['items']['br_chestkey'])

# Kitchen

# Living Room

####################### DECLARE ENTITY OBJECTS #######################
# Bedroom
br_bed = Entity(**object_data['entities']['br_bed'])
br_chest = Entity(**object_data['entities']['br_chest'])

# Kitchen

# Living Room

####################### DECLARE ROOM OBJECTS #######################
# Bedroom
bedroom = Room(**object_data['rooms']['bedroom'])