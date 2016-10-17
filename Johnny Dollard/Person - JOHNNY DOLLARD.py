'''
Johnny Dollard
Period 4
Assignment: Person Lab
'''
import pygame
from pygame.locals import *


# Create a class called Person
class Person:
    
    # Create a constructor method that sets self.x to newX, 
    # self.y to newY and loads the image "dude.gif" into self.img
    def __init__ (self,newX,newY):
        self.x=newX
        self.y=newY
        self.img=pygame.image.load("dude.gif")
    # draw the image on the surface
    def draw(self):
        pass
    
    def moveLeft(self):
        # Change x so that the object can move left
        pass

    def moveRight(self):
        # Change x so that the object can move right
        pass

    def moveUp(self):
        # Change y so that the object can move up
        pass

    def moveDown(self):
        # Change y so that the object can move down
        pass

