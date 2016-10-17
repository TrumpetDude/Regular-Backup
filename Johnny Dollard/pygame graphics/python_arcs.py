import pygame
import sys
from math import pi

pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)
r1 = ((10, 10), (100, 100))
r2 = ((20, 60), (200, 60))
r3 = ((15,15), (100,100))
pygame.draw.arc(screen, green, r1, 0, pi/2, 2)
#pygame.draw.arc(screen, red, r2, 0, pi, 5)
pygame.draw.arc(screen, blue, r3, pi, 2*pi, 3)
#pygame.draw.arc(surface, color, rect, start point RADIANS, stop point RADIANS, thickness)

# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT ):
              pygame.quit(); 
              sys.exit();
            

