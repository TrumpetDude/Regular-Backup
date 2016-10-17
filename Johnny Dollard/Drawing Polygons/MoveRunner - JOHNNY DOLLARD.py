'''
Johnny Dollard
Period 4
Assignment: Person Lab
'''
import pygame, sys
from pygame.locals import *
from Person import *
from random import randint

# Creates the screen to draw on
pygame.init()
window = pygame.display.set_mode((800,600))

# Allows a key that is held down to count as multiple presses
pygame.key.set_repeat(1,1)

color=(randint(0,255),randint(0,255),randint(0,255)

pygame.draw.rect(window,color,[100,150,50,25]))

# Colors the screen white
red=randint(0,255)
green=randint(0,255)
blue=randint(0,255)
def windowFill(red,green,blue):
    window.fill((red,green,blue))
windowFill(255,255,255)
    
# Event Loop
while True:
    
    windowFill(red,green,blue)
    
    # Draw your person on the screen
    guy.draw(window)
    
    # Update the screen
    pygame.display.update()


    # Check for key presses and mouse clicks
    for event in pygame.event.get():
        # Determine if the user has closed the window or pressed escape
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            # Quit the program
            pygame.quit()
            sys.exit()
        
        # Check if an arrow key is pressed and 
        # move guy in the correct direction
        elif event.type==KEYDOWN:

            if event.key==K_UP: 
                guy.moveUp()

            elif event.key==K_DOWN:
                guy.moveDown()

            elif event.key==K_LEFT:
                guy.moveLeft()

            elif event.key==K_RIGHT:
                guy.moveRight()

            elif  event.key==K_SPACE:
                red=randint(0,255)
                green=randint(0,255)
                blue=randint(0,255)
                windowFill(red,green,blue)
                
