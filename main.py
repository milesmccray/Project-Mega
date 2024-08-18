import pygame
from player import Player
from rooms import Bedroom
from entity import Entity
from item import Item


class Game:
    def __init__(self):
        pygame.init()

        # Screen Setup
        self.screenW = 1080
        self.screenH = 720
        pygame.display.set_caption('Project Mega Demo')
        self.display = pygame.display.set_mode((self.screenW, self.screenH))

        # Initialize Player Object
        self.player = Player('Test Man')  # Player name

        # Create Starting Room and Initialize
        self.demo = Bedroom()
        self.player.update_room(self.demo)

    def run(self):
        while True:
            self.display.blit(self.player.current_room_bg, (0, 0))
            pygame.display.update()

            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for entity in self.player.current_room.entities:  # Collision check for entities in current room
                        if entity.position.collidepoint(pygame.mouse.get_pos()):  # If collision do...
                            print(entity.description)
                            self.event_window(entity)

                    for item in self.player.current_room.items:       # Collision check for items in current room
                        if item.position.collidepoint(pygame.mouse.get_pos()):    # If collision do...
                            print(item.description)
                            self.event_window(item)

                if event.type == pygame.QUIT:
                    pygame.quit()

    def event_window(self, interactable: Item | Entity):
        """Takes in Item/Entity object and displays what events are available"""
        for event in interactable.events:
            print(event)


Game().run()
