import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
window = pygame.display.set_mode((1300,700))
pygame.display.set_caption("Undersea Adventure","Undersea Adventure")
pygame.key.set_repeat(1,1)

def drawText(window, text, size, color, centerX, centerY):
    font=pygame.font.Font("comicSansMS.ttf", size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)
def done(window):
    pygame.draw.line(window,(0,60,120),(0,350),(1300,350),200)
    drawText(window, "Are you sure you want to quit? Your Progress will not be saved.",42,(100,120,255),650,300)
    drawText(window, "Yes                 No",54,(100,120,255),650,385)
    pygame.draw.rect(window, (100,120,255), (424,355,110,65), 5)
    pygame.draw.rect(window, (100,120,255), (777,355,110,65), 5)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        mousePos=pygame.mouse.get_pos()
        mousePressed=pygame.mouse.get_pressed()
        if mousePos[1]>355 and mousePos[1]<420 and mousePos[0]>777 and mousePos[0]<887 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            break
        if mousePos[1]>355 and mousePos[1]<420 and mousePos[0]>424 and mousePos[0]<534 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            pygame.quit()
            sys.exit(0)

background = pygame.image.load("backGround.gif")
clam = pygame.image.load("clam.gif")
bubble = pygame.image.load("bubble.gif")
fish1R = pygame.image.load("1FishRight.gif")
fish1L = pygame.image.load("1FishLeft.gif")

shipUP = clam
shipLEFT = pygame.transform.rotate(shipUP, 90.0)
shipDOWN = pygame.transform.rotate(shipLEFT, 90.0)
shipRIGHT = pygame.transform.rotate(shipDOWN, 90.0)
shipX = randint(0,1234)
shipY = randint(0,634)
shooters = 1
speed = 0.25                         #INITIAL SPEED
ticks = 0
ship = shipUP
inU = 0
inD = 0
inR = 0
inL = 0
bubble1 = False
bubble2 = False
bubble3 = False
bubbleDelayAmount = 100              #SINGLE BUBBLE CANNON FIRE RATE
bubbleDelay = -bubbleDelayAmount-1
fish1OnScreen = False


while True:
    
    ticks+=1
    mousePos=pygame.mouse.get_pos()
    mousePressed=pygame.mouse.get_pressed()
    window.blit(background,(0,0))

    #bubbleAimX=(mousePos[0]+shipX)/2
    #bubbleAimY=(mousePos[1]+shipY)/2

    #Make Fish 1
    if not(fish1OnScreen) and randint(0,150) == 1:
        fish1OnScreen = True
        if randint(0,1) == 0:
            direction = -1
            fish1X = 1300
            fish1 = fish1L
        else:
            direction = 1
            fish1X = -64
            fish1 = fish1R
        fish1Y = randint(0, 652)
    
    #Bubble Shooting
    if sum(mousePressed) > 0 and ticks-bubbleDelay>bubbleDelayAmount/shooters:
            if True:
                bubble1 = True
                bubbleX1 = shipX-12
                bubbleY1 = shipY-12
                slope = 0
                b1x = 0
                b1y = 0
                if not(mousePos[0] == shipX):
                    slope = (mousePos[1]-shipY)/(mousePos[0]-shipX)
                if abs(slope) < 0.3:
                    b1x = 6
                    b1y = 0
                elif abs(slope) < 1:
                    b1x = 5
                    b1y = 2.5
                elif abs(slope) < 2:
                    b1x = 3.2
                    b1y = 3.2
                elif abs(slope) < 4:
                    b1x = 2.5
                    b1y = 5
                else:
                    b1x = 0
                    b1y = 6
                if mousePos[1] < shipY:
                        b1y *= -1
                if mousePos[0] < shipX:
                    b1x *= -1
                bubbleDelay = ticks
            if shooters >= 2:
                bubble2 = True
                bubbleX2 = shipX-12
                bubbleY2 = shipY-12
                slope = 0
                b2x = 0
                b2y = 0
                if not(mousePos[0] == shipX):
                    slope = (mousePos[1]-shipY)/(mousePos[0]-shipX)
                if abs(slope) < 0.3:
                    b2x = 6
                    b2y = 0
                elif abs(slope) < 1:
                    b2x = 5
                    b2y = 2.5
                elif abs(slope) < 2:
                    b2x = 3.2
                    b2y = 3.2
                elif abs(slope) < 4:
                    b2x = 2.5
                    b2y = 5
                else:
                    b2x = 0
                    b2y = 6
                if mousePos[1] < shipY:
                    b2y *= -1
                if mousePos[0] < shipX:
                    b2x *= -1
                bubbleDelay = ticks
            if shooters >= 3:
                bubble3 = True
                bubbleX3 = shipX-12
                bubbleY3 = shipY-12
                slope = 0
                b3x = 0
                b3y = 0
                if not(mousePos[0] == shipX):
                    slope = (mousePos[1]-shipY)/(mousePos[0]-shipX)
                if abs(slope) < 0.3:
                    b3x = 6
                    b3y = 0
                elif abs(slope) < 1:
                    b3x = 5
                    b3y = 2.5
                elif abs(slope) < 2:
                    b3x = 3.2
                    b3y = 3.2
                elif abs(slope) < 4:
                    b3x = 2.5
                    b3y = 5
                else:
                    b3x = 0
                    b3y = 6
                if mousePos[1] < shipY:
                    b3y *= -1
                if mousePos[0] < shipX:
                    b3x *= -1
                bubbleDelay = ticks

    #Fish1 Stuff
    if fish1OnScreen:
        fish1X += direction
        window.blit(fish1, (fish1X, fish1Y))
        if fish1X < -65 or fish1X > 1301:
            fish1OnScreen = False
        if bubble1 and bubbleX1-fish1X<68 and bubbleX1-fish1X>-24 and fish1Y-bubbleY1>-44 and fish1Y-bubbleY1<24:
            fish1OnScreen = False
            bubble1 = False
            
    #Event Detection
    for event in pygame.event.get():
        if (event.type==KEYUP and event.key==K_ESCAPE) or event.type==QUIT:
            done(window)
                

                    
    #Movement
    keys=pygame.key.get_pressed()
    if keys[K_w]:
            if shipY > 90:
                ship = shipUP
                inU += 0.1*speed
                inD -= 0.05*speed

    if keys[K_s]:
            if shipY < 652:
                ship = shipDOWN
                inD += 0.1*speed
                inU -= 0.05*speed

    if keys[K_a]:
            if shipX > 1:
                ship = shipLEFT
                inL += 0.1*speed
                inR -= 0.05*speed

    if keys[K_d]:
            if shipX < 1255:
                ship = shipRIGHT
                inR += 0.1*speed
                inL -= 0.05*speed
    #Inertia
    inU -= 0.05*speed
    inD -= 0.05*speed
    inL -= 0.05*speed
    inR -= 0.05*speed
    if inU<0:
        inU=0
    if inD<0:
        inD=0
    if inL<0:
        inL=0
    if inR<0:
        inR=0
    shipX += inR
    shipY += inD
    shipX -= inL
    shipY -= inU
    if shipY < 90:
        inU -= 0.1
        inD += 0.1
    if shipY > 668:
        shipY -= 1
        inU += 0.05
        inD -= 0.05
    if shipX < 32:
        shipX += 1
        inR += 0.05
        inL -= 0.05
    if shipX > 1268:
        shipX -= 1
        inL += 0.05
        inR -= 0.05


    if bubble1:
        bubbleX1 += b1x
        bubbleY1 += b1y
        window.blit(bubble, (bubbleX1, bubbleY1))
        if bubbleX1>1300 or bubbleX1<-24 or bubbleY1>700 or bubbleY1<-24:
            bubble1=False
    if bubble2:
        bubbleX2 += b2x
        bubbleY2 += b2y
        window.blit(bubble, (bubbleX2, bubbleY2))
        if bubbleX2>1300 or bubbleX2<-24 or bubbleY2>700 or bubbleY2<-24:
            bubble2=False
    if bubble3:
        bubbleX3 += b3x
        bubbleY3 += b3y
        window.blit(bubble, (bubbleX3, bubbleY3))
        if bubbleX3>1300 or bubbleX3<-24 or bubbleY3>700 or bubbleY3<-24:
            bubble3=False
        
    window.blit(ship, (shipX-32, shipY-32))
    #pygame.draw.line(window, (0,0,0), (shipX,shipY), (bubbleAimX,bubbleAimY), 1)
    #aiming line
    pygame.display.update()
