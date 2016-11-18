import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((800,600))
walk=pygame.image.load("walk_sign.GIF")
dontWalk=pygame.image.load("dont_walk_sign.GIF")
redLight=False
yellowLight=False
greenLight=True
cross=False

while True:
    window.fill((127,127,127))
    pygame.draw.rect(window, (0,127,0), (0,0,800,20),0)
    pygame.draw.rect(window, (0,127,0), (0,580,800,20),0)
    pygame.draw.circle(window, (30,0,0), (50,80), 30, 0)
    pygame.draw.circle(window, (30,0,0), (750,375), 30, 0)
    pygame.draw.circle(window, (25,20,0), (50,145), 30, 0)
    pygame.draw.circle(window, (25,20,0), (750,440), 30, 0)
    pygame.draw.circle(window, (0,255,0), (50,210), 30, 0)
    pygame.draw.circle(window, (0,255,0), (750,505), 30, 0)
    window.blit(dontWalk, (300,530))
    pygame.draw.rect(window, (255,255,255), (450,50,40,40),0)
    pygame.display.update()
    mousePos=pygame.mouse.get_pos()
    mousePressed=pygame.mouse.get_pressed()
    

    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()

        if mousePos[1]>50 and mousePos[1]<90 and mousePos[0]>450 and mousePos[0]<490 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            pygame.time.delay(4000)
            #Green Off
            pygame.draw.circle(window, (0,20,0), (50,210), 30, 0)
            pygame.draw.circle(window, (0,20,0), (750,505), 30, 0)
            #Yellow on
            pygame.draw.circle(window, (255,255,0), (50,145), 30, 0)
            pygame.draw.circle(window, (255,255,0), (750,440), 30, 0)

            pygame.display.update()
            pygame.time.delay(2000)
                
            #Yellow Off
            pygame.draw.circle(window, (25,20,0), (50,145), 30, 0)
            pygame.draw.circle(window, (25,20,0), (750,440), 30, 0)
            #Red On
            pygame.draw.circle(window, (255,0,0), (50,80), 30, 0)
            pygame.draw.circle(window, (255,0,0), (750,375), 30, 0)

            pygame.display.update()
            pygame.time.delay(2000)
                
            window.blit(walk, (300,530))

            pygame.display.update()
            pygame.time.delay(8000)

            pygame.draw.rect(window, (127,127,127), (300,530,50,50),0)
            window.blit(dontWalk, (300,530))

            pygame.display.update()
            pygame.time.delay(2000)
                
            #Red Off
            pygame.draw.circle(window, (30,0,0), (50,80), 30, 0)
            pygame.draw.circle(window, (30,0,0), (750,375), 30, 0)
