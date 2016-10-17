import pygame, time, sys
from random import randint


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)

pygame.draw.rect(screen, green, (10,10,50,50), 3)
pygame.draw.rect(screen, red, (50,100,80,60), 7)
pygame.draw.rect(screen, green, (13,13,600,68), randint(0,10))
pygame.draw.rect(screen, red, (23,154,24,305), randint(0,10))
pygame.draw.rect(screen, blue, (93,27,303,289), randint(0,10))
# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT ):
              pygame.quit(); 
              sys.exit();
            

