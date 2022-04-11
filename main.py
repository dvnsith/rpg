#!/usr/bin/python3
import time


def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    An RPG game
    ========
    Commands:
      go [direction]
      get [item]
      fight

    ''')


def showStatus():
    """determine the current status of the player"""
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'north': 'Bedroom',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Bathroom',
    },
    'Bedroom': {
        'south': 'Hall',
        'item': 'note'
    },
    'Kitchen': {
        'north': 'Hall',
        'east': 'Cabinet',
        'south': 'Garage',
        'item': 'spider',
    },
    'Cabinet': {
        'west': 'Kitchen',
        'item': 'wallet'
    },
    'Garage': {
        'north': 'Kitchen',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Backyard',
        'item': 'car key'
    },
    'Backyard': {
        'north': 'Dining Room',
        'west': 'Tool shed'
    },
    'Bathroom': {
        'east': 'Hall',
        'north': 'Closet',
        'item': 'hairspray'
    },
    'Closet': {
        'south': 'Bathroom',
        'item': 'lighter'
    },
    'Tool shed': {
        'east': 'Backyard'
    }
}


isLocked = True
# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# loop forever
while True:
    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # If a player has the neccessary items to make a weapon
    if currentRoom == 'Tool shed' and isLocked:
        print("Can't access tool shed.\nLooks like there's a lock")
        if 'note' in inventory:
            time.sleep(2)
            print('Opening note...')
            time.sleep(2)
            lockCombination = input(
                'When was python first released?\na. Febuary 21, 1995\nb. December 4. 1995\nc. Febuary 21, 1991\nd. January 23, 1995\n> ').lower()
            if lockCombination == 'c':
                print("Unlocked!")
                time.sleep(2)
                print("Let's take a look at your inventory...")
                isLocked = False
                if 'lighter' in inventory and 'hairspray' in inventory:
                    time.sleep(2)
                    print("Looks like you can make a flamethrower")
                    inventory.remove("lighter")
                    inventory.remove("hairspray")
                    inventory.append("flamethrower")
                else:
                    time.sleep(2)
                    print("There is nothing worth making.")
                inventory.remove('note')
            else:
                time.sleep(2)
                print("Incorrect code, come back and try again")
                currentRoom = 'Backyard'
        else:
            currentRoom = 'Backyard'

    # If a player enters a room with a spider
    if 'item' in rooms[currentRoom] and 'spider' in rooms[currentRoom]['item']:
        print("You have encountered a HUGE spider!")
        time.sleep(2)
        question = input("Would you like to do? \n>")
        answerBank1 = ['go back', 'go north']
        answerBank2 = ['fight', 'continue']
        if question in answerBank1:
            currentRoom = 'Hall'
        elif question in answerBank2 and 'flamethrower' in inventory:
            del rooms[currentRoom]['item']
            inventory.remove('flamethrower')
            time.sleep(2)
            print('You have used a flamethrower to kill the spider')

        else:
            print('The spider has eaten you alive... GAME OVER!')
            break

        # Define how a player can win
    if currentRoom == 'Garage' and 'car key' in inventory and 'wallet' in inventory:
        print("YOU WIN! You escaped the house to get groceries. BTW pick up some raid.")
        break
