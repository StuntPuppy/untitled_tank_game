#Chapter 10 Lab
#Natalie Gotham
#CSC2000
#Displays a cursor on the screen corresponding to keyboard, mouse, and joystick input if present

import pygame
import math
#for keyboard input detection
from pygame.locals import *

# Define some basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
#Custom colors
#Friendly force
SAND = (242,210,169)
#Opposing force
ARMYGREEN = (41,92,61)
#Airstrike reticle color
AFBLUE = (32,42,120)
 
def draw_tank(screen, x, y):
    #tank body
    pygame.draw.rect(screen, SAND, [-25 + x, -37 + y, 50, 75], 0)
    
    #outlining by drawing 4x 1 wide rects offset by 1 pixel in each direction
    pygame.draw.rect(screen, BLACK, [-24 + x, -37 + y, 50, 75], 1)
    pygame.draw.rect(screen, BLACK, [-26 + x, -37 + y, 50, 75], 1)
    pygame.draw.rect(screen, BLACK, [-25 + x, -38 + y, 50, 75], 1)
    pygame.draw.rect(screen, BLACK, [-25 + x, -36 + y, 50, 75], 1)
    
    #tank turret
    
    #barrel
    pygame.draw.rect(screen, SAND, [-5 + x, -70 + y, 10, 60], 0)
    #barrel outline
    pygame.draw.rect(screen, BLACK, [-5 + x, -70 + y, 10, 60], 1)  
    
    #turret body
    pygame.draw.ellipse(screen, SAND, [-20 + x, -20 + y, 40, 40], 0)
    
    #outlining
    pygame.draw.ellipse(screen, BLACK, [-19 + x, -20 + y, 40, 40], 1)
    pygame.draw.ellipse(screen, BLACK, [-21 + x, -20 + y, 40, 40], 1)
    pygame.draw.ellipse(screen, BLACK, [-20 + x, -19 + y, 40, 40], 1)
    pygame.draw.ellipse(screen, BLACK, [-20 + x, -21 + y, 40, 40], 1)
    

    
    
def draw_reticle(screen, x, y):
    #Draw an aiming reticle at x, y 
    
    # Center ring
    #starting offset of 5 pixels above and to the left of x/y
    pygame.draw.ellipse(screen, BLACK, [-5 + x, -5 + y, 10, 10], 2)
 
    # Legs
    #Top Right
    pygame.draw.line(screen, BLACK, [10 + x, -5 + y], [20 + x, -10 + y], 5)
    #Bottom Right
    pygame.draw.line(screen, BLACK, [10 + x, 5 + y], [20 + x, 10 + y], 5)
    
    #Top Left
    pygame.draw.line(screen, BLACK, [-10 + x, -5 + y], [-20 + x, -10 + y], 5)
    #Bottom Left
    pygame.draw.line(screen, BLACK, [-10 + x, 5 + y], [-20 + x, 10 + y], 5)
    
def draw_strike_reticle(screen, x, y):
    #Draw an airstrike reticle at x, y
    
    # Center ring
    pygame.draw.ellipse(screen, RED, [-9 + x, -9 + y, 19, 19], 2)
    
    #Center Ring reticle lines
    #Left
    pygame.draw.line(screen, RED, [-9 + x, y], [-5 + x, y], 2)
    #Right
    pygame.draw.line(screen, RED, [9 + x, y], [5 + x, y], 2)
    #Top
    pygame.draw.line(screen, RED, [x, -9 + y], [x, -5 + y], 2)
    #Bottom
    pygame.draw.line(screen, RED, [x, 9 + y], [x, 5 + y], 2)
    
    #Blue pointed segments
     
    #Top Left
    pygame.draw.line(screen, AFBLUE, [x, -10 + y], [-10 + x, -20 + y], 5)
    #Top Right
    pygame.draw.line(screen, AFBLUE, [x, -10 + y], [10 + x, -20 + y], 5)
    
    #Bottom Left
    pygame.draw.line(screen, AFBLUE, [x, 10 + y], [-10 + x, 20 + y], 5)
    #Bottom Right
    pygame.draw.line(screen, AFBLUE, [x, 10 + y], [10 + x, 20 + y], 5)

    #Right Upper
    pygame.draw.line(screen, AFBLUE, [10 + x, y], [20 + x, -10 + y], 5)
    #Right Lower
    pygame.draw.line(screen, AFBLUE, [10 + x, y], [20 + x, 10 + y], 5)
    
    #Left Upper
    pygame.draw.line(screen, AFBLUE, [-10 + x, y], [-20 + x, -10 + y], 5)
    #Left Lower
    pygame.draw.line(screen, AFBLUE, [-10 + x, y], [-20 + x, 10 + y], 5)
 
pygame.init()
pygame.joystick.init()

"""
initialized to true so the user can be prompted for configuration prior to 
main game loop loading
"""
done = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Count the joysticks the computer has
joystick_count = pygame.joystick.get_count()

#declaring screen size so the center can be determined
size = [800, 600]

if joystick_count == 0:
    # No joysticks!
    print("No joysticks present on the system, moving forward with keyboard and mouse control.")
    #allow game loop to run
    done = False
    
else:
    #Initialize storage variable as -1 in order to both enumerate the indices and store the last appended index
    joyIndex = -1
        
    #initializing a list of all joysticks the system can see
    joysticks = [pygame.joystick.Joystick(i) for i in range (pygame.joystick.get_count())]    
    
    print("\nDetected joysticks:\n")
        
    #show the names of each joystick in order
    for joystick in joysticks:
        #advance to 0 in preparation for printing
        joyIndex += 1
        print(f"Joy [{joyIndex}]: {joystick.get_name()}")

    #Ask the user which joystick they'd like to use
    userJoyChoice = input(f"\nWhich joystick # would you like to use?(0 - {joyIndex}): ")
    #convert to int so it can be used as an index
    userJoyChoice = int(userJoyChoice)
    my_joystick = joysticks[userJoyChoice]
    #allow game loop to run
    done = False
    
    # starting position for joystick
    # center of the screen
    x_coord_joy = (size[0] / 2) - 1
    y_coord_joy = (size[1] / 2) - 1
    
"""
#screen center starting coords for keyboard
x_coord_kb = (size[0] / 2) - 1
y_coord_kb = (size[1] / 2) - 1
"""

#Player tank start point
x_coord_kb = 50
y_coord_kb = 500

x_speed_kb = 0
y_speed_kb = 0

screen = pygame.display.set_mode(size)

# Hide the mouse cursor
pygame.mouse.set_visible(False)
    
while not done:
 
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        # User pressed down on a key   
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True               
            # Figure out if it was an arrow key. If so
            # adjust speed.                
            elif event.key == pygame.K_LEFT:
                x_speed_kb = -3
            elif event.key == pygame.K_RIGHT:
                x_speed_kb = 3
            elif event.key == pygame.K_UP:
                y_speed_kb = -3
            elif event.key == pygame.K_DOWN:
                y_speed_kb = 3
            
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed_kb = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed_kb = 0
             

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
    
    #Breaking the rules a bit and putting the screen.fill above the joystick
    #processing in order to have the joystick crosshair be drawn conditionally
    screen.fill(WHITE)
    
    #Mouse handling
    #Get and store mouse position
    mousepos = pygame.mouse.get_pos()
    mousex = mousepos[0]
    mousey = mousepos[1]    
        
    #Keyboard movement
    x_coord_kb += x_speed_kb
    y_coord_kb += y_speed_kb
    
    
    #Keyboard Boundary Handling
    if x_coord_kb <= 26:
        x_speed_kb = 0
        x_coord_kb = 26
        
    if x_coord_kb >= 774:
        x_speed_kb = 0
        x_coord_kb = 774   
        
    if y_coord_kb <= 69:
        y_speed_kb = 0
        y_coord_kb = 69
        
    if y_coord_kb >= 561:
        y_speed_kb = 0
        y_coord_kb = 561
        

    
    # Draw tank at kb cursor coordinates
    # Draw tank first so crosshairs overlay the tank
    draw_tank(screen, x_coord_kb, y_coord_kb) 
    
    # Draw crosshair at mouse coordinates
    draw_reticle(screen, mousex, mousey)

    # As long as there is a joystick
    if joystick_count != 0:
 
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
 
        # Move x according to the axis. Multiplied by 5
        # to speed up the movement.
        x_coord_joy = x_coord_joy + int(horiz_axis_pos * 5)
        y_coord_joy = y_coord_joy + int(vert_axis_pos * 5)
        
        
        #Joystick Boundary handling
        if x_coord_joy <= 22:
            x_coord_joy = 22
    
        if x_coord_joy >= 777:
            x_coord_joy = 777
            
        if y_coord_joy <= 20:
            y_coord_joy = 20
            
        if y_coord_joy >= 579:
            y_coord_joy = 579
            
            
        # Draw airstrike crosshair at joystick coordinates
        draw_strike_reticle(screen, x_coord_joy, y_coord_joy) 
 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()