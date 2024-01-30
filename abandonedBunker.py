"""
Chapter 7 Lab
Abandoned nuclear bunker
Inspired by Zork and the S.T.A.L.K.E.R. game series, themselves inspired by the book "Roadside Picnic", by Arkady and Boris Strugatsky
Bare Minimum(tm) edition

I misunderstood a couple of pieces of the instructions and vastly overcomplicated this
for myself in the beginning. This is the pared down version to follow the instructions,
with some additional input validation
"""

import time
import sys

#Create empty list to store rooms
room_list = []

#Initialize empty list room each time to create a new list in memory
room = [None] * 5

#Room 0 - Outside
room[0] = "You are following a trail north through the woods, and the trail ends at what appears to be the door to an abandoned fallout shelter."
room[1] = 1
room[2] = None
room[3] = None
room[4] = None

room_list.append(room)

room = [None] * 5

#Room 1 - Common Area
room[0] = "You are in the common area. There are rusty metal doors to the North, South, East, and West. The North door hangs slightly ajar."
room[1] = 2
room[2] = 4
room[3] = 0
room[4] = 3

room_list.append(room)

room = [None] * 5

#Room 2 - Infirmary
room[0] = "You are in the Infirmary. There is a single exam table in the middle of the room, a desk in the far corner and medical supplies lining the back wall. There are doors leading East, South, and West."
room[1] = None
room[2] = 6
room[3] = 1
room[4] = 5

room_list.append(room)

room = [None] * 5

#Room 3 - Women's Sleeping Area
room[0] = "You enter a sleeping area akin to a military barracks. Only bedframes and some scattered women's clothing remains. There are doors leading North and East."
room[1] = 5
room[2] = 1
room[3] = None
room[4] = None

room_list.append(room)

room = [None] * 5

#Room 4 - Men's Sleeping Area
room[0] = "You enter a sleeping area akin to a military barracks. Only bedframes and some scattered men's clothing remains. There are doors leading North and West."
room[1] = 6
room[2] = None
room[3] = None
room[4] = 1

room_list.append(room)

room = [None] * 5

#Room 5 - Bulk storage
room[0] = "You are in a bulk storage area. The room is a mess of empty shelves, crates, and boxes. There are doors leading North and East."
room[1] = 7
room[2] = 2
room[3] = 3
room[4] = None

room_list.append(room)

room = [None] * 5

#Room 6 - Armory
room[0] = "You are in an Armory. There were once weapons in the racks on the wall, but all that remains are some empty shell casings on the ground and some wires on a desk where a radio once sat. There are doors leading West and South."
room[1] = None
room[2] = None
room[3] = 4
room[4] = 2

room_list.append(room)

room = [None] * 5

#Room 7 - Food Storage
room[0] = "You are in a food storage room that stretches the length of the building. A deep, guttural growl emanates from the darkness at the far end of the room."
room[1] = None
room[2] = 8
room[3] = 5
room[4] = None

room_list.append(room)

room = [None] * 5

#Room 8 - Doom
room[0] = "You bravely venture into the darkness. You hear a monstrous roar, and it would prove be the last thing you ever heard. Another lost to the Zone."
room[1] = None
room[2] = None
room[3] = None
room[4] = 7

room_list.append(room)

current_room = 0

done = False

while not done:
    
    #If you're in the food storage room and choose to go east, towards the growling        
    if current_room == 8:
        #You die
        print(room_list[current_room][0])
        
        restart_choice = input("Would you like to play again? [Y/n]: ")
        
        if restart_choice.upper() == "YES" or restart_choice.upper() == "Y":
            #reset current room to beginning
            current_room = 0
            print()
            print("Your pain quickly fades from memory.")
            print()
            continue
        
        elif restart_choice.upper() == "NO" or restart_choice.upper() == "N":
            done = True
            break
        else:
            print("Please enter Yes or No")
    #print turn information and prompt player for action
    print(room_list[current_room][0])
    player_choice = input("Where would you like to go? ")
    print()
    
    #Input validation
    
    #split the player's choice into a list of words
    #enables the player to input sentences in response
    #like "Go through the North door."
    #by ignoring all words but those matching directions
    choice_words = player_choice.split()
    direction_word_counter = 0
    
    for word in choice_words:
        if word.upper() == "NORTH" or word.upper() == "N":
            chosen_direction = word.upper()
            direction_word_counter += 1
            
        if word.upper() == "EAST" or word.upper() == "E":
            chosen_direction = word.upper()
            direction_word_counter += 1

        if word.upper() == "SOUTH" or word.upper() == "S":
            chosen_direction = word.upper()
            direction_word_counter += 1

        if word.upper() == "WEST" or word.upper() == "W":
            chosen_direction = word.upper()
            direction_word_counter += 1
       
        if direction_word_counter > 1:
            break
            

    #if no directions are given or are mispelled, re-prompt player for direction
    if direction_word_counter == 0:
        print()
        print("I'm sorry, I don't understand. You didn't enter a direction.")
        print()
        continue
    #if more than one directional input is given, remind the player "one at a time"
    #and restart the loop    
    if direction_word_counter > 1:
        print()
        print("Please, only one direction at a time.")
        print()
        continue    
    
    if chosen_direction == "NORTH" or chosen_direction == "N":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You cannot go that way.")
        else:
            current_room = next_room
            
    elif chosen_direction == "EAST" or chosen_direction == "E":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You cannot go that way.")
        else:
            current_room = next_room
            
    elif chosen_direction == "SOUTH" or chosen_direction == "S":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You cannot go that way.")
        else:
            current_room = next_room
            
    elif chosen_direction == "WEST" or chosen_direction == "W":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You cannot go that way.") 
        else:
            current_room = next_room
            


#Thank the user, give a few seconds to see the message, and exit the program
print("\nThanks for exploring the bunker, see you next time!")
time.sleep(3)
sys.exit()