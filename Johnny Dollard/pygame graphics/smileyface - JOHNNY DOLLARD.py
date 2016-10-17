'''
Johnny Dollard
Programming 1
Pygame Lab
'''
import pygame
import sys
from math import pi


pygame.init()

screen = pygame.display.set_mode((640,480))

white = (255,255,255)
screen.fill(white)

yellow = (255,255,0)
orange = (255,69,0)
green = (0, 255, 0)
blue=(0, 0, 255)
red = (255, 0 , 0)
eye1=(180,70,100,70)
eye2=(330,70,100,70)
nose=((300,150),(325,200),(275,200))
mouthArc=((170,150),(250,200))
# draw a smiley face

# draw eyes
pygame.draw.ellipse(screen, green,eye1,3)
pygame.draw.ellipse(screen, green,eye2,3)
# draw a nose
pygame.draw.polygon(screen, red, nose, 5)
# draw a mouth
pygame.draw.arc(screen, orange, mouthArc, pi, 2*pi+0.05, 3)
pygame.draw.line(screen, orange,(170,250),(419,250), 3)
#Do fun extra stuff
pygame.draw.circle(screen, blue, (300, 200), 200, 5)
# update the screen
pygame.display.update()

while (True):
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT ):
              pygame.quit(); 
              sys.exit();
            

