from room import Room
from player import Player
from item import Item
import os

# Declare all the rooms
room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

# Main
#

# Make a new player object that is currently in the 'outside' room.

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

name = input("Enter your player's name: ")
player = Player(name, room["outside"])
current_room = player.current_room

print(f"Welcome, {name} to this Adventure Game!")
os.system("clear")

game_running = True

def wrong_direction():
    print("There isn't anything this way!")
    os.system("clear")

while game_running:
    print(f"{name}'s current location: {player.current_room.name} ({player.current_room.description})")

    user_choice = input("Choose a direction to move.  Enter n (North), s (South), e (East), w (West), or q (quit): ").lower()
    if user_choice == "n":
        if hasattr(player.current_room, "n_to"):
            player.current_room = player.current_room.n_to
            print(f"{name} went North.")
            os.system("clear")
        else:
            wrong_direction()
    elif user_choice == "s":
        if hasattr(player.current_room, "s_to"):
            player.current_room = player.current_room.s_to
            print(f"{name} went South.")
            os.system("clear")
        else:
            wrong_direction()
    elif user_choice == "e":
        if hasattr(player.current_room, "e_to"):
            player.current_room = player.current_room.e_to
            print(f"{name} went East.")
            os.system("clear")
        else:
            wrong_direction()
    elif user_choice == "w":
        if hasattr(player.current_room, "w_to"):
            player.current_room = player.current_room.w_to
            print(f"{name} went West.")
            os.system("clear")
        else:
            wrong_direction()
    elif user_choice == "q":
        print("Thanks for playing. Now exiting game.")
        game_running = False
    else:
        print("Not a valid direction.")