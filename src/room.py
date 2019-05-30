# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.room_description = room_description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.room_items = []

    def get_directions(self, direction):
        if direction == "n":
            return self.n_to
        if direction == "s":
            return self.s_to
        if direction == "e":
            return self.e_to
        if direction == "w":
            return self.w_to

    def __repr__(self):
        returnString = (f"""----------------------------\n
                Name: {self.room_name},
                \nDescription: {self.room_description}
                \n---------------------------------------""")
        return returnString

    def remove_item(self, select_item):
        print("\nroom items++++++", self.room_items)
        print("\nselect item", select_item)
        self.items = self.room_items.remove(select_item)

    def add_item(self, select_item):
        self.items = self.room_items.insert(0, select_item)
