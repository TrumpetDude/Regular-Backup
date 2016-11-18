'''
Johnny Dollard
Period 4
Assignment: Loops Lab 5
'''
import pygame, random
from pygame.locals import *

# draw the grass and rocks
def draw(window):
    # Load grass.gif and rock.gif into variables
    grass=pygame.image.load("grass.gif")
    rock=pygame.image.load("rock.gif")

    # Outer loop runs as long as x is 
    # not past the right edge of the screen
    for grassX in range(0,800,50):
        # Inner loop runs as long as y is 
        # not past the bottom edge of the screen
        for grassY in range(0,600,50):
            # Draws the grass and increases the y
            window.blit(grass, (grassX,grassY))
    
    
    # Draw 30 rocks in random x and y positions
    for rockNum in range(30):
        window.blit(rock, (random.randint(0,777),random.randint(0,587)))
