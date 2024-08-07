import json
import os.path


class Player:
    def __init__(self, name='Default Joe'):
        # Load player save if it exists, else create new Player object
        if os.path.isfile('data/player_save.json'):
            self.load_player()
        else:
            self.name = name
            self.inventory = []
            self.current_room = None

    def add_item(self, item: str):
        self.inventory.append(item)

    def remove_item(self, item: str):
        self.inventory.remove(item)

    def update_room(self, room: str):
        self.current_room = room

    def save_player(self):
        player_save = {'name': self.name, 'inventory': self.inventory, 'current_room': self.current_room}

        with open('data/player_save.json', 'w') as f:
            json.dump(player_save, f, indent=4)

    def load_player(self):
        with open('data/player_save.json', 'r') as f:
            player_data = json.load(f)
        try:
            self.name = player_data['name']
            self.inventory = player_data['inventory']
            self.current_room = player_data['current_room']
        except KeyError:
            print('corrupt save file...')
            #TODO: What if save file is corrupt? Handle this appropriately.
