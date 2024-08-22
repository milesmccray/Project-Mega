import pygame
import sys
from player import Player
from rooms import Bedroom
from entity import Entity
from item import Item

# TODO: Need to rework hitbox collision after adding in nav bar

class Game:
    def __init__(self):
        pygame.init()

        # Screen Setup
        self.SCALE = 6
        self.resolutionW = 256
        self.resolutionH = 144
        self.screenW = (self.resolutionW * self.SCALE) # 1536px Scales up resolution to screen window size
        self.screenH = self.resolutionH * self.SCALE  # 864px  Scales up resolution to screen window size
        self.screen = pygame.display.set_mode((self.screenW, self.screenH))  # Window Surface
        self.px_display = pygame.Surface((self.resolutionW, self.resolutionH))  # Display to be scaled to Screen size

        self.nav_bar = pygame.image.load('data/menus/events.png')
        self.nav_bar_w = 35 * self.SCALE
        self.nav_bar_h = 52 * self.SCALE

        pygame.display.set_caption('Project Mega Demo')

        # Create Objects and Initialize
        self.player = Player('Test Man')
        self.demo = Bedroom()  # Starting Room
        self.player.update_room(self.demo)

    def run(self):
        while True:
            self.px_display.blit(self.player.current_room_bg, (0, 0))

            # Event Handler
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for entity in self.player.current_room.entities:  # Collision check for entities in current room
                        if entity.position.collidepoint(self.mouse_position()):  # If collision do...
                            self.event_window(entity)

                    for item in self.player.current_room.items:  # Collision check for items in current room
                        if item.position.collidepoint(self.mouse_position()):  # If collision do...
                            self.event_window(item)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Scales the display to the size of the window
            scale_room = pygame.transform.scale(self.px_display, (self.screenW - self.nav_bar_w, self.screenH))
            scale_nav = pygame.transform.scale(self.nav_bar, (self.nav_bar_w, self.nav_bar_h))

            # Blits the new scaled display to the main window surface
            self.screen.blit(scale_room, (0, 0))
            self.screen.blit(scale_nav, (self.screenW - self.nav_bar_w, 0))
            pygame.display.update()

    def event_window(self, interactable: Item | Entity):
        """Takes in Item/Entity object and displays what events are available"""
        for event, value in interactable.events.items():
            if event == 'inventory' and value:
                print('can be added to inventory')
            if event == 'usable' and value:
                print(interactable.description)
            if event == 'container' and value:
                print('this is a container')
            if event == 'door' and value:
                print('this is a door')

    def mouse_position(self):
        """Returns a scaled down mouse position to match resolution"""
        return [round(i / self.SCALE) for i in pygame.mouse.get_pos()]


Game().run()
