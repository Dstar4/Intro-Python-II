from room import Room
from player import Player
from item import Item
# Declare All Items


items = {
    'candle': Item('candle', 'a normal candle'),
    'hat': Item('hat', 'an everyday hat'),
    'binoculars': Item('binoculars', 'for looking at distant memories.'),
    'matches': Item('matches', 'A pack of matches, these could come in handy.'),
    'cobwebs': Item('cobwebs', 'Can you really ever get them off of you?')
}

# Declare all the rooms

room = {
    'outside': Room('Outside the shack',
                    '''Its foundations sinking into the earth, shutters falling off the windows,\
The porch, in true country fashion wraps allthe way around the house.'''),

    'foyer': Room('On the front porch',
                  '''Dim light filters in from the house.\
The porch wraps around the house to the the North, or you\
can enter the house to the East.'''),

    'overlook': Room(' On the Back porch',
                     '''The back porch looks over a swamp spanning as far as the eye can see.\
There is no way through.'''),

    'narrow': Room(' in the Cabin',
                   '''The cabin is dark, only lit by a candle in the middle of the room.\
There is the faint smell of musty air coming from the \
cellar to the North.'''),

    'treasure': Room('in the Cellar',
                     '''You enter the cellar, you are not sure what you came\
for, but you do not see anything of interest here.'''),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Set items

# room['outside'].items = ['shovel', 'spade']
room['outside'].items = items['candle'], items['hat']
room['overlook'].items = items['binoculars'], items['matches']
room['narrow'].items = items['cobwebs']
#
# Main
#
# Make a new player object that is currently in the 'outside' room.
player = Player('Daniel', room['outside'])

valid_input = ('n', 's', 'e', 'w')

while True:
    print(f'{player.current_room}')
    userDirection = input(
        'Please choose a direction to travel: n,s,e,w\t')

    if userDirection in valid_input:
        if player.current_room.get_directions(userDirection) is None:
            print('You cannot travel that way.')
        else:
            player.travel(userDirection)

    elif userDirection == 'i':
        print(item.item_name for item in player.inventory)

    elif userDirection == 'q':
        break

    elif userDirection == 'take':
        select = input(
            'Please enter the name of the item you with to pick up.')
        print("SELECT", select)
        print(player.current_room.items)
        if select in player.current_room.item_names:
            print("items in adv", select)
            player.current_room.remove_item(select)
            # player.take_item(items[select])
            # print(items[select].pick_up())
        else:
            print("\nItem is not in this room.")

    elif userDirection == 'drop':
        select = input(
            '--------------------------------\nPlease enter the name of the\
item you with to drop.\n')
        print('select', select)

        # player.drop_item(select)
        # player.current_room.add_item(select)

    else:
        print('Please enter a valid direction.')
