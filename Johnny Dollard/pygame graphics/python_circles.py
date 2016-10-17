import pygame, sys, time
from random import randint


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)
p1 = (50, 50)
p2 = (150, 100)

pygame.draw.circle(screen, green, p1, 15, 2)
pygame.draw.circle(screen, red, p2, 30, 5)

# update the screen
pygame.display.update()

while (True):
    pygame.draw.circle(screen, red, (randint(1,640), randint(1,480)), randint(10,100),randint(0,9))
    pygame.draw.circle(screen, green, (randint(1,640), randint(1,480)), randint(10,100),randint(0,9))
    pygame.draw.circle(screen, blue, (randint(1,640), randint(1,480)), randint(10,100),randint(0,9))
    pygame.display.update()
    time.sleep(0.1)
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT ):
              pygame.quit(); 
              sys.exit();
            

