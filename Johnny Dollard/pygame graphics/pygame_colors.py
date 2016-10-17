# all imports go at the top
import pygame, sys, random


# create the screen
pygame.init()
screen = pygame.display.set_mode((800,600))


# Colors the screen a random color
r  = random.randint(0, 256)
g = random.randint(0, 256)
b = random.randint(0, 256)
randColor  = ( r, g, b )
screen.fill( randColor )

# Updates the display
pygame.display.update()
           
while True:
    for event in pygame.event.get() :
         if event.type == pygame.QUIT:
              pygame.quit(); 
              sys.exit();
            
