from item import Item
import rooms
import pygame


class Player:
    def __init__(self, name='Default Joe'):
        self.name = name
        self.inventory = []
        self.current_room = None
        self.current_room_bg = None

    def add_item(self, item: Item):
        self.inventory.append(item)

    def remove_item(self, item: Item):
        self.inventory.remove(item)

    def update_room(self, room: rooms):
        """Loads the image string in JSON file to current room"""
        self.current_room = room
        self.current_room_bg = pygame.image.load(room.image)
