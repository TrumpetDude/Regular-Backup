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
        self.img = pygame.draw.rect(window,color,[x,y,height,width]))
        

    # draw the image on the surface
    def draw(self, window):
        window.blit(self.img,(self.x,self.y))
    
        
    
    def moveLeft(self):
        # Change x so that the object can move left
        if self.x>1:
            self.x=self.x-1
        return self.x
    

    def moveRight(self):
        # Change x so that the object can move right
        if self.x<750:
            self.x=self.x+1
        return self.x
    
       

    def moveUp(self):
        # Change y so that the object can move up
        if self.y>1:
            self.y=self.y-1
        return self.y
    

    
    def moveDown(self):
        # Change y so that the object can move down
        if self.y<550:
            self.y=self.y+1
        return self.y
        
