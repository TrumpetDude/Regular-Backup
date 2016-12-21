#Setup
import pygame, sys
from pygame.locals import *
from random import randint, uniform
pygame.init()
window = pygame.display.set_mode((1300,700))#,pygame.FULLSCREEN)
pygame.display.set_caption("Zombie Apocalypse","Zombie Apocalypse")
pygame.key.set_repeat(1,1)
from array import array
from time import sleep
from pygame.mixer import Sound, get_init, pre_init
from zombieMethods import *

    
#Initialize Variables
ticks=0
HP=100
score=0
baseSpeed=6
speedStart=-501
infectStart=-2001
infectAmount=0
guyX=randint(0,1250)
guyY=randint(0,650)
red=0
green=0
blue=0
HPr=0
HPg=255
doubleSpeedOnScreen=False
plusHealthOnScreen=False
zombies = []

#Load Images
zombie=pygame.image.load("zombie.gif")
chestOpened=pygame.image.load("chestOpened.gif")
dude=pygame.image.load("dude.gif")
dudeDamaged=pygame.image.load("dudeDamaged.gif")
chest=pygame.image.load("chest.gif")
doubleSpeed=pygame.image.load("doubleSpeed.gif")
plusHealth=pygame.image.load("health.gif")



while HP>0:
    ticks+=1

    drawAlways(window, score, HP, HPr, HPg, zombies)
    
    #Make Double Speed
    if not(doubleSpeedOnScreen) and randint(1,600)==1 and ticks-speedStart>500:
        doubleSpeedOnScreen=True
        speedX=randint(0,1267)
        speedY=randint(0,667)
    #Make +Health
    if not(plusHealthOnScreen) and randint(1,800)==1:
        plusHealthOnScreen=True
        healthX=randint(0,1267)
        healthY=randint(0,667)
    #Make Zombie
    if randint(1,500)==1:
        playSound(220,100)
        zombies.append([randint(0,1250),randint(0,650),uniform(2,5)])

    #Draw and Move Double Speed
    if doubleSpeedOnScreen:
        window.blit(doubleSpeed, (speedX, speedY))
        if speedX<1:
            speedX=1
        if speedX>1254:
            speedX=1254
        if speedY<2:
            speedY=2
        if speedY>652:
            speedY=652
        if speedX<=guyX:
            speedX-=2
        elif speedX>=guyX:
            speedX+=2
        if speedY<=guyY:
            speedY-=2
        elif speedY>=guyY:
            speedY+=2
    #Draw and Move +Health
    if plusHealthOnScreen:
        window.blit(plusHealth, (healthX, healthY))
        if healthX<1:
            healthX=1
        if healthX>1254:
            healthX=1254
        if healthY<2:
            healthY=2
        if healthY>652:
            healthY=652
        if healthX<=guyX:
            healthX-=2
        elif healthX>=guyX:
            healthX+=2
        if healthY<=guyY:
            healthY-=2
        elif healthY>=guyY:
            healthY+=2


    #Pick up Double Speed
    if doubleSpeedOnScreen and speedX-guyX<48 and speedX-guyX>-32 and guyY-speedY>-48 and guyY-speedY<32:
        playSound(264, 50)
        doubleSpeedOnScreen=False
        speedStart=ticks
        score+=50
    #Pick up +Health
    if plusHealthOnScreen and healthX-guyX<48 and healthX-guyX>-32 and guyY-healthY>-48 and guyY-healthY<32:
        playSound(293.333333, 50)
        plusHealthOnScreen=False
        score+=50
        HP+=5
        if HP>100:
            HP=100
        infectStart=ticks-2001

    #Take damage from infection
    if ticks-infectStart<2000:
        window.blit(dudeDamaged, (guyX,guyY))
        HP-= infectAmount
    else:
        window.blit(dude,(guyX,guyY))
    

    
    #Get Infected by Zombie
    for z in zombies:
        if z[0]-guyX<48 and z[0]-guyX>-48 and guyY-z[1]>-48 and guyY-z[1]<48 and randint(1,100) == 1:
            playSound(55, 100)
            zombies.pop(0)
            HP-=5
            infectAmount += 0.015
            infectStart=ticks

        
    #Change HP text color
    if HP>=50:
        HPr=0+5*(100-HP)
    else:
        HPr=255
    if HPr==255:
        HPg=255-5*(50-HP)

    #Move and draw Zombies
    for z in zombies:
        if z[0]<guyX:
            z[0]+=uniform(1,z[2])
        elif z[0]>guyX:
            z[0]-=uniform(1,z[2])
        if z[1]<guyY:
            z[1]+=uniform(1,z[2])
        elif z[1]>guyY:
            z[1]-=uniform(1,z[2])
        window.blit(zombie, (z[0], z[1]))


    #Regen HP
    if HP<100-0.006:
        HP+=0.006
    else:
        HP=100

    #Increase score
    score+=len(zombies)

        
    # Update the screen
    pygame.display.update()
        
    # Check for key presses
    for event in pygame.event.get():
            if (event.type==KEYUP and event.key==K_ESCAPE)or event.type==QUIT:
                done(window)
        
            # Check if an arrow key is pressed and 
            # move guy in the correct direction
            keys = pygame.key.get_pressed()
            if ticks-speedStart<500:
                speed=baseSpeed*2
            else:
                speed=baseSpeed

            if keys[K_w]:
                if guyY>1:
                    guyY-=speed

            if keys[K_s]:
                if guyY<652:
                    guyY+=speed

            if keys[K_a]:
                if guyX>1:
                    guyX-=speed

            if keys[K_d]:
                if guyX<1255:
                    guyX+=speed

            if keys[K_EQUALS]:#Make zombies manually              
                playSound(220,100)
                zombies.append([randint(0,1250),randint(0,650),uniform(2,5)])
                                 
gameOver(window)
