from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

#
# Main
#

def get_dir(cmd, current_room):
    if cmd == 'n':
        return current room.n_to
    elif cmd == 's':
        return current room.s_to
    elif cmd == 'e':
        return current room.e_to
    elif cmd == 'w':
        return current room.w_to

player = Player(room['outside'])

print("Entera key to continue... \n [n]orth, [s]outh, [e]ast, [w]est \n -or- [q]quit")

directions = ['n','s', 'e', 'w']

# Make a new player object that is currently in the 'outside' room.

while True:
    print(player.current_room)
    print(player.current_room.description)
    cmd = input("Your Command -> ")

    if cmd in directions:
        get_dir(cmd, player.current_room)
    elif cmd == 'q':
        break
    else:
        print('Bad Command, My Liege!')

    

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
