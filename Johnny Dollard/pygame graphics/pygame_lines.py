import pygame, sys, time
from random import randint

pygame.init()
screen = pygame.display.set_mode((640,480))


white = (255,255,255)
screen.fill(white)

green = (0, 255, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)

point1 = ( 50, 50 )
point2 = ( 150, 150 )

pygame.draw.line(screen, green, point1, point2)

point1 = ( 50, 100 )
point2 = ( 50, 150 )
pygame.draw.line(screen, red, point1, point2)


# update the screen
pygame.display.update()

while (True):
    point1 = ( randint(1,640), randint(1,480) )
    point2 = ( randint(1,640), randint(1,480) )
    pygame.draw.line(screen, red, point1, point2, randint(0,5))
         
    point1 = ( randint(1,640), randint(1,480) )
    point2 = ( randint(1,640), randint(1,480) )
    pygame.draw.line(screen, green, point1, point2, randint(0,5))
         
    point1 = ( randint(1,640), randint(1,480) )
    point2 = ( randint(1,640), randint(1,480) )
    pygame.draw.line(screen, blue, point1, point2, randint(0,5))

    pygame.display.update();

    time.sleep(0.1);
    
    for event in pygame.event.get() :
         if ( event.type == pygame.QUIT ):
              pygame.quit(); 
              sys.exit();
                          

