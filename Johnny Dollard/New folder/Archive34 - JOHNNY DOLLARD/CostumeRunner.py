'''
Johnny Dollard
Period 4
List Lab 4
'''
import pygame, sys
from pygame.locals import *
from Person import *

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode((800,600))

# allows user to hold down the key to move
pygame.key.set_repeat(1, 1)


# create a person named guy
guy = Person(50,50)

# A list that keeps track of the areas of screen that have changed
changedRecs=[]

#draw the starting screen
screen.fill((255,255,255))
pygame.display.update()


#Event Loop
while True:
    # draw the scene
    screen.fill((255,255,255))
    
    guy.draw(screen)
    
    # adds the current position of guy to the areas that have been changed
    changedRecs.append(guy.getRec())
    
    #update only the changed areas of the screen
    pygame.display.update(changedRecs)

    # check for events
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        elif event.type==KEYDOWN:
            #add the old position of guy to the areas of guy that have been changed
            changedRecs.append(guy.getRec())
            
            if event.key==K_UP: 
                guy.moveUp()

            elif event.key==K_DOWN:
                guy.moveDown()

            elif event.key==K_LEFT:
                guy.moveLeft()

            elif event.key==K_RIGHT:
                guy.moveRight()
