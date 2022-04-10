#!/usr/bin/python3

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
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Bathroom',
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
        'west': 'Kitchen',
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
        'item': 'hair spray'
    },
    'Closet': {
        'south': 'Bathroom',
        'item': 'lighter'
    },
    'Tool shed': {
        'east': 'Backyard'
    }
}


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

    if currentRoom == 'Tool shed':
        print("Let's take a look at your inventory...")
        if 'lighter' in inventory and 'hair spray' in inventory:
            print("Looks like you can make a flamethrower")
            inventory.remove("lighter")
            inventory.remove("hair spray")
            inventory.append("flamethrower")
        else:
            print("There is nothing worth making.")

    # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'spider' in rooms[currentRoom]['item']:
        print("You have encountered a HUGE spider!")
        question = input("Would you like to do? \n>")
        answerBank1 = ['go back', 'go north', 'return']
        answerBank2 = ['fight', 'continue']
        if question in answerBank1:
            currentRoom = 'Hall'
        elif question in answerBank2 and 'flamethrower' in inventory:
            del rooms[currentRoom]['item']
            inventory.remove('flamethrower')
            print('You have used a flamethrower to kill the spider')

        else:
            print('The spider has eaten you alive... GAME OVER!')
            break

        # Define how a player can win
    if currentRoom == 'Garage' and 'car key' in inventory and 'wallet' in inventory:
        print("YOU WIN! You escaped the house to get groceries. BTW pick up some raid.")
        break
