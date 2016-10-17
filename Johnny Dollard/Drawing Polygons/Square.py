import pygame, sys
from pygame.locals import *
import time
from random import randint
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.key.set_repeat(1,1)
height=50
width=50
x=0
y=0
r=randint(0,256)
g=randint(0,256)
b=randint(0,256)
OBJECTCOLOR=((r,g,b))
SCREENCOLOR=((265-r,265-g,256-b))
screen.fill(SCREENCOLOR)
while True:
    screen.fill(SCREENCOLOR)
    pygame.draw.rect(screen, OBJECTCOLOR,[x,y,height,width])
    pygame.display.update()

    # Check for key presses and mouse clicks
    for event in pygame.event.get():
        # Determine if the user has closed the window or pressed escape
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            # Quit the program
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:

            if event.key==K_UP:
                y=y-1

            elif event.key==K_DOWN:
                y=y+1

            elif event.key==K_LEFT:
                x=x-1

            elif event.key==K_RIGHT:
                x=x+1
            
            elif  event.key==K_SPACE:
                r=randint(1,255)
                g=randint(1,255)
                b=randint(1,255)
                OBJECTCOLOR=((r,g,b))
                SCREENCOLOR=((256-r,256-g,256-b))
            
            elif event.key==K_d:
                height=height+1

            elif event.key==K_a:
                height=height-1

            elif event.key==K_s:
                width=width+1
                
            elif event.key==K_w:
                width=width-1
            
