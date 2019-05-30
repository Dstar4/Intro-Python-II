# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_description, items=[]):
        self.room_name = room_name
        self.room_description = room_description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = items
        self.item_names = items

    def __repr__(self):
        items = []
        for item in self.items:
            items.append(item.item_name)
        else:
            print("no items")
        # print("\n\nitems in room", items)

        returnString = (f"""--------------------------------------------------------------------\
\n{self.room_name},
{self.room_description}
\nGlancing around you see, {items}
\n--------------------------------------------------------------------""")
        returnString += f"\nYou may travel [{self.getRoomExitString()}]\n"
        return returnString

    def get_directions(self, direction):
        if direction == "n":
            return self.n_to
        if direction == "s":
            return self.s_to
        if direction == "e":
            return self.e_to
        if direction == "w":
            return self.w_to

    def getRoomExitString(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return ", ".join(exits)

    def remove_item(self, select_item):
        print("\nroom items++++++", self.items)
        self.items.remove(select_item)
        print("\nselect item", self.items)

    def add_item(self, select_item):
        self.items = self.items.insert(0, select_item)
