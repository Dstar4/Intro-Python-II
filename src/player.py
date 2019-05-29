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

    def __repr__(self):
        return f'Name: {player_name}, Current Room: {current_room}'

    def travel(self, direction):
        if direction == "n":
            self.current_room = self.current_room.n_to
        if direction == "s":
            self.current_room = self.current_room.s_to
        if direction == "e":
            self.current_room = self.current_room.e_to
        if direction == "w":
            self.current_room = self.current_room.w_to
