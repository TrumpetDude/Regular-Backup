import pygame, sys
from pygame.locals import *

import random
keyRepeatSpeed=10
'''
x=0
y=0
img=pygame.image.load("dude.gif")
'''
def arrowUp(red, green, blue):
    print("KEY UP")
def arrowDown(red, green, blue):
    print("KEY DOWN")
def arrowRight():
    print("KEY RIGHT")
def arrowLeft():
    print("KEY LEFT")
    
#Create Screen
pygame.init()
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)
screenLength=random.randint(1,1800)
screenWidth=random.randint(1,2400)
pygame.key.set_repeat(10,10)


#Event loop
while True:

    #Sets dimensions of screen
    screen = pygame.display.set_mode((screenWidth,screenLength))

    #Colors the screen
    screen.fill((red,green,blue))
    
    #Draw person on screen
    #guy.draw(screen)

    #Update the screen
    pygame.display.update()

    #Check for key presses and mouse clicks
    for event in pygame.event.get():
        #Check for close window or esc
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            #Quit the program
            pygame.quit()
            sys.exit()

        #Check for arrow and move guy
        elif event.type==KEYDOWN:

            if event.key==K_UP:
                arrowUp(red, green, blue)   

            if event.key==K_DOWN:
                arrowDown(red, green, blue)

            if event.key==K_LEFT:
                arrowLeft()

            if event.key==K_RIGHT:
                arrowRight()

            if event.key==K_RSHIFT:
                pass

            if event.key==K_RETURN:
                pass
