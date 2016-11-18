'''
Johnny Dollard
Period 4
Assignment: Loops Lab 4
'''
import pygame
from pygame.locals import *

def drawSquares(window):
    # Create variables to keep track of size and position
    squareX=0
    squareY=0
    # Use a loop to draw squares until the size is too small
    for size in range(100,0,-10):
        pygame.draw.rect(window, (0,0,255), (squareX,squareY,size,size))
        squareY+=10
        squareX+=size+10
        
        
def drawCircles(window):
    # Create variables to keep track of size, position and color
    radius=100
    green=255
    # Use a loop to draw circles until the size is too small
    while radius>0:
        pygame.draw.circle(window, (0,green,0), (300,300), radius)
        radius-=10
        green-=25
