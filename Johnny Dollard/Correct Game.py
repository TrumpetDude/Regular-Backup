import pygame, sys
from pygame.locals import *
import random

#Create Screen
pygame.init()
#Delay on key repeats
pygame.key.set_repeat(1,1)
#Sets dimensions of screen
screen = pygame.display.set_mode((800,600))
x=0
y=0
img=pygame.image.load("dude.gif")

x=random.randint(1,750)
y=random.randint(1,550)
img = pygame.image.load("dude.gif")

def arrowUp(y):
    if y>1:
        y=y-1
    return y
def arrowDown(y):
    if y<550:
        y=y+1
    return y
def arrowRight(x):
    if x<750:
        x=x+1
    return x
def arrowLeft(x):
    if x>1:
        x=x-1
    return x

#Event loop
while True:
    #Colors the screen
    screen.fill((255,255,255))
        
    #Draw person on screen
    #guy.draw(screen)
    screen.blit(img, (x,y))
    
    #Update the screen
    pygame.display.update()
    
    z=y
    w=x
    
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
                y=arrowUp(y)
                
            elif event.key==K_DOWN:
                y=arrowDown(y)

            elif event.key==K_LEFT:
                x=arrowLeft(x)

            elif event.key==K_RIGHT:
                x=arrowRight(x)
