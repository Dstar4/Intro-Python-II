from room import Room
from player import Player


class Item:
    def __init__(self, item_name, item_description, starting_location,
                 is_light):
        # super().__init__(current_room)
        self.item_name = item_name
        self.item_description = item_description
        self.location = starting_location
        if is_light is True:
            self.lightsource = True
            print("lightsource", self.lightsource)
        else:
            self.lightsource = False

    # def __repr(self):
        # return f'Item: {self.item_name}'

    def on_take(self, item):
        # player.get_item(item)
        return(f'You have picked up {item}. Behold its glory.')

    def on_drop(self, item):
        return(f'You have dropped {item}.')
