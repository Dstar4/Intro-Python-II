from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room('Outside the shack',
                     '''You stand outside the shack.\
Its foundations sinking into the earth, shutters falling off the windows,\
beginning to grow a sort of moss. The porch, in true country fashion wraps all\
the way around the house.'''),

    'foyer':    Room('on the Porch',
                     '''Dim light filters in from the house.\
The porch wraps around the house to the the North, or you\
can enter the house to the East.'''),

    'overlook': Room(' on the Back Porch',
                     '''The back porch looks over a swamp spanning as far as the eye can see.\
There is no way through.'''),

    'narrow':   Room(' in the Cabin',
                     '''The cabin is dark, only lit by a candle in the middle of the room.\
 There is the faint smell of musty air coming from the \
cellar to the North.'''),

    'treasure': Room('in the Cellar',
                     '''You enter the cellar, you are not sure what you came\
for, but you do not see anything of interest here.'''),
}

# Declare All Items

item = {
    'candle': Item('Candle', 'a normal candle', 'Outside', True)
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
room['outside'].items = item['candle']
# room['overlook'].items = ['binoculars', 'matches']
# room['narrow'].items = ['cobwebs']
#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player('Daniel', room['outside'])
# Write a loop that:
#


valid_input = ['n', 's', 'e', 'w']


while True:

    print(f'\nYou are now {player.current_room.room_name}')
    if player.current_room.items:
        print(f'{player.current_room.room_description},\n\
            Items: {player.current_room.items.item_name} \n')
    userDirection = input(
        'Please choose a direction to travel: n,s,e,w\n')

    if userDirection in valid_input:
        if player.current_room.get_directions(userDirection) is None:
            print('You cannot travel that way.')
        else:
            player.travel(userDirection)
    elif userDirection == 'i':
        print(player.inventory)
    elif userDirection == 'q':
        break
    elif userDirection == 'take':
        select = input(
            'Please enter the name of the item you with to pick up.')

        # print('select', select)
        # player.inventory.on_take(select)
        # player.get_item(select)
        # player.current_room.remove_item(select)
        # player.lightsource = True
        if userDirection == 'drop':
            select = input(
                'Please enter the name of the item you with to drop.\n')
    elif userDirection == 'drop':
        select = input(
            'Please enter the name of the item you with to drop.\n')
        print('select', select)
        player.drop_item(select)
        player.current_room.add_item(select)

    else:
        print('Please enter a valid direction.')

    # TODO REPL Class
'''
- Print Name and Description of Current Room after movement.
- n , s , e , w are valid commands for movement
- Print item list of current room.
- Understand Verb , Object input.
- i command for inventory.
'''
