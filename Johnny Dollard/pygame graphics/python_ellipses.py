import pygame, time, sys
from random import randint

pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)
r1 = (50, 10, 50, 100)
r2 = (90, 20, 100, 200)

pygame.draw.ellipse(screen, green, r1, 2)
pygame.draw.ellipse(screen, red, r2, 5)

# update the screen
pygame.display.update()

while (True):
    pygame.draw.ellipse(screen, red, (1,1,randint(10,640),randint(10,480)), randint(0,5))
    pygame.draw.ellipse(screen, blue, (1,1,randint(10,640),randint(10,480)), randint(0,5))
    pygame.draw.ellipse(screen, green, (1,1,randint(10,640),randint(10,480)), randint(0,5))
    pygame.display.update()
    time.sleep(0.1)
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT ):
              pygame.quit(); 
              sys.exit();
            

