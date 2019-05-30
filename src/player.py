# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room
# TODO Player Class
'''
Name
Current Room
Inventory
'''


class Player:
    def __init__(self, player_name, starting_room):
        self.player_name = player_name
        self.current_room = starting_room
        self.inventory = ["hat", "monocle", ]
        self.lightsource = None

    def __repr__(self):
        return f'Name: {self.player_name}, Current Room: {self.current_room}'

    def travel(self, direction):
        if direction == "n":
            self.current_room = self.current_room.n_to
        if direction == "s":
            self.current_room = self.current_room.s_to
        if direction == "e":
            self.current_room = self.current_room.e_to
        if direction == "w":
            self.current_room = self.current_room.w_to

    def get_item(self, item):
        self.inventory.insert(0, item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def add_light(self, bool):
        if bool is True:
            print("You have found a lightsource")
            self.lightsource = True
