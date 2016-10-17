import pygame, random

def drawScene(window):
    # Loads an image
    img = pygame.image.load("dude.gif")

    
    # Draws the image on the screen that is passed to it
    window.blit(img, (30,40))
    

    # This will draw a circle a random spot
    pygame.draw.circle(window, (255,0,0),(random.randint(100,400),random.randint(0,300)), 50)


    # This will draw a rectangle a random spot
    pygame.draw.rect(window, (0,255,0),(random.randint(100,400),random.randint(0,300), 150, 150))