import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)
r1 = ((50, 10), (50, 100), (30, 30))
r2 = ((100, 20), (200, 70), (50, 50))

pygame.draw.polygon(screen, green, r1, 2)
pygame.draw.polygon(screen, red, r2, 5)

# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT ):
              pygame.quit(); 
              sys.exit();
            

