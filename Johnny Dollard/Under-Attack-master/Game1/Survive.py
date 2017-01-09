#Setup
import pygame, sys
from pygame.locals import *
from random import randint
pygame.init()
window = pygame.display.set_mode((1300,700), pygame.FULLSCREEN)
pygame.display.set_caption("Survive","Survive")
pygame.key.set_repeat(1,1)
from array import array
from time import sleep
import pygame
from pygame.mixer import Sound, get_init, pre_init
from tone import Note

#Methods
def windowFill(red,green,blue):
    window.fill((red,green,blue))
def drawText(text, size, color, centerX, centerY):
    font=pygame.font.Font("PressStart2P.ttf", size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)
def playSound(hz,ms):
    pre_init(44100, -16, 1, 1024)
    Note(hz).play(ms)
def done():
    pygame.draw.line(window,(50,50,50),(0,350),(1300,350),200)
    drawText("Are you sure you want to quit? Your Progress will not be saved.",20,(200,200,200),650,300)
    drawText("Yes               No",24,(200,200,200),650,400)
    pygame.draw.rect(window, (200,200,200), (395,375,100,50), 5)
    pygame.draw.rect(window, (200,200,200), (815,375,100,50), 5)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        mousePos=pygame.mouse.get_pos()
        mousePressed=pygame.mouse.get_pressed()
        if mousePos[1]>375 and mousePos[1]<425 and mousePos[0]>815 and mousePos[0]<915 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            break
        if mousePos[1]>375 and mousePos[1]<425 and mousePos[0]>395 and mousePos[0]<495 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            pygame.quit()
            sys.exit(0)
def level2():
    pygame.draw.line(window,(50,50,50),(0,350),(1300,350),200)
    drawText("You have completed Level 1!",20,(200,200,200),650,300)
    drawText("Continue",24,(200,200,200),650,400)
    pygame.draw.rect(window, (200,200,200), (540,375,220,50), 5)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYUP and event.key == K_ESCAPE):
                done()
        mousePos=pygame.mouse.get_pos()
        mousePressed=pygame.mouse.get_pressed()
        if mousePos[1]>375 and mousePos[1]<425 and mousePos[0]>540 and mousePos[0]<760 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            import zombieApocalypse
#Initialize Variables
ticks=0
HP=100
coins=0
score=0
baseSpeed=1
speedStart=-501
damageStart=-501
infectStart=-2001
zombieStart=-2501
regenSpeed=0.001
guyX=randint(0,1250)
guyY=randint(0,650)
red=0
green=0
blue=0
HPr=0
HPg=255
coinOnScreen=False
chestOnScreen=False
doubleSpeedOnScreen=False
plusHealthOnScreen=False
DEOnScreen=False
DDOnScreen=False
enemy1OnScreen=False
enemy2OnScreen=False
zombieOnScreen=False
enemy1HP=0
enemy2HP=0
zombieHP=0

#Load Images
enemy1=pygame.image.load("enemy1.gif")
enemy1damaged=pygame.image.load("enemy1damaged.gif")
enemy2=pygame.image.load("enemy2.gif")
enemy2damaged=pygame.image.load("enemy2damaged.gif")
zombie=pygame.image.load("zombie.gif")
zombieDamaged=pygame.image.load("zombieDamaged.gif")
chestOpened=pygame.image.load("chestOpened.gif")
dude=pygame.image.load("dude.gif")
dudeDamaged=pygame.image.load("dudeDamaged.gif")
chest=pygame.image.load("chest.gif")
doubleSpeed=pygame.image.load("doubleSpeed.gif")
plusHealth=pygame.image.load("health.gif")
destroyEnemies=pygame.image.load("destroyEnemies.gif")
doubleDamage=pygame.image.load("doubleDamage.gif")



while HP>0:
    ticks+=1
    
    #Draw Background and words
    windowFill(red,green,blue)
    pygame.draw.rect(window, (50,50,50), (0,0,315,50),0)
    pygame.draw.line(window,(0,0,0) ,(125,0), (125,50), 5)
    drawText("+ SPEED: 1",12,(0, 0, 255),50,25)
    drawText("+ HP REGEN: 2",12,(255, 0, 255),220,25)
    drawText("COINS: "+str(coins), 26, (255,255,0),650,20)
    drawText("HP: "+str(int(HP//1)), 26, (HPr, HPg, 0),650,50)
    drawText("SCORE: "+str(score), 26, (255,255,255),1100,20)
    if enemy1OnScreen or enemy2OnScreen or zombieOnScreen:
        drawText("TOTAL ENEMY HP: "+str(int(enemy1HP//1)+int(enemy2HP//1)+int(zombieHP//1)), 26, (255,0,0),650,80)

    #Make Coin
    if not(coinOnScreen) and randint(1,333)==1:
        coinOnScreen=True
        coinX=randint(10,1290)
        coinY=randint(10,690)
    #Make Chest
    if not(chestOnScreen) and randint(1,7500)==1:
        chestOnScreen=True
        chestX=randint(16,1200)
        chestY=randint(1,639)
    #Make Double Speed
    if not(doubleSpeedOnScreen) and randint(1,750)==1 and ticks-speedStart>500:
        doubleSpeedOnScreen=True
        speedX=randint(0,1267)
        speedY=randint(0,667)
    #Make +Health
    if not(plusHealthOnScreen) and randint(1,1500)==1:
        plusHealthOnScreen=True
        healthX=randint(0,1267)
        healthY=randint(0,667)
    #Make Destroy Enemies
    if not(DEOnScreen) and randint(1,5000)==1:
        DEOnScreen=True
        DEX=randint(0,1267)
        DEY=randint(0,667)
    #Make Double Damage
    if not(DDOnScreen) and randint(1,750)==1:
        DDOnScreen=True
        DDX=randint(0,1267)
        DDY=randint(0,667)
    #Make Enemy1
    if not(enemy1OnScreen) and randint(1,1000)==1:
        enemy1OnScreen=True
        enemy1X=randint(0,1260)
        enemy1Y=randint(0,660)
        enemy1HP=10
    #Make Enemy2
    if not(enemy2OnScreen) and randint(1,1000)==1:
        enemy2OnScreen=True
        enemy2X=randint(0,1260)
        enemy2Y=randint(0,660)
        enemy2HP=20
    #Make Zombie
    if not(zombieOnScreen) and randint(1,1000)==1:
        zombieOnScreen=True
        zombieX=randint(0,1250)
        zombieY=randint(0,650)
        zombieHP=20
        zombieStart=ticks
        
    #Draw Coin
    if coinOnScreen:
        pygame.draw.circle(window, (255,255,0),(coinX,coinY),8,0)
    #Draw Chest
    if chestOnScreen:
        window.blit(chest, (chestX, chestY))
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
            speedX-=1
        elif speedX>=guyX:
            speedX+=1
        if speedY<=guyY:
            speedY-=1
        elif speedY>=guyY:
            speedY+=1
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
            healthX-=1
        elif healthX>=guyX:
            healthX+=1
        if healthY<=guyY:
            healthY-=1
        elif healthY>=guyY:
            healthY+=1
    #Draw and Move Destroy Enemies
    if DEOnScreen:
        window.blit(destroyEnemies, (DEX, DEY))
        if DEX<1:
            DEX=1
        if DEX>1254:
            DEX=1254
        if DEY<2:
            DEY=2
        if DEY>652:
            DEY=652
        if DEX<=guyX:
            DEX-=1
        elif DEX>=guyX:
            DEX+=1
        if DEY<=guyY:
            DEY-=1
        elif DEY>=guyY:
            DEY+=1
    #Draw and Move Double Damage
    if DDOnScreen:
        window.blit(doubleDamage, (DDX, DDY))
        if DDX<1:
            DDX=1
        if DDX>1254:
            DDX=1254
        if DDY<2:
            DDY=2
        if DDY>652:
            DDY=652
        if DDX<=guyX:
            DDX-=1
        elif DDX>=guyX:
            DDX+=1
        if DDY<=guyY:
            DDY-=1
        elif DDY>=guyY:
            DDY+=1
        
        
    #Pick up Coin
    if coinOnScreen and coinX-guyX<60 and coinX-guyX>-5 and guyY-coinY>-60 and guyY-coinY<10:
        playSound(220, 50)
        coinOnScreen=False
        coins+=1
        score+=10
        playSound(220, 50)
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
    #Pick up Destroy Enemies
    if DEOnScreen and DEX-guyX<48 and DEX-guyX>-32 and guyY-DEY>-48 and guyY-DEY<32:
        playSound(307.375, 50)
        DEOnScreen=False
        enemy1HP=0
        enemy2HP=0
        zombieHP=0
        if enemy1OnScreen:
            coins+=10
            score+=250
        if enemy2OnScreen:
            coins+=25
            score+=500
        if zombieOnScreen:
            coins+=30
            score+=750
        enemy1OnScreen=False
        enemy2OnScreen=False
        zombieOnScreen=False
        score+=50
    #Pick up Double Damage
    if DDOnScreen and DDX-guyX<48 and DDX-guyX>-32 and guyY-DDY>-48 and guyY-DDY<32:
        playSound(330, 50)
        DDOnScreen=False
        damageStart=ticks
        score+=50


    #Take damage from infection
    if ticks-infectStart<2000:
        window.blit(zombie, (guyX,guyY))
        HP-=0.015
    else:
        window.blit(dude,(guyX,guyY))
    

    
    #Take damage from enemy1
    if enemy1OnScreen and enemy1X-guyX<48 and enemy1X-guyX>-32 and guyY-enemy1Y>-48 and guyY-enemy1Y<32:
        HP-=0.25
        if ticks-infectStart<2000:
            window.blit(zombieDamaged,(guyX,guyY))
        else:
            window.blit(dudeDamaged,(guyX,guyY))
    #Take damage from enemy2
    if enemy2OnScreen and enemy2X-guyX<48 and enemy2X-guyX>-32 and guyY-enemy2Y>-48 and guyY-enemy2Y<32:
        HP/=2
        window.blit(dudeDamaged,(guyX,guyY))
        enemy2OnScreen=False
        enemy2HP=0
    #Get Infected by Zombie
    if zombieOnScreen and zombieX-guyX<48 and zombieX-guyX>-48 and guyY-zombieY>-48 and guyY-zombieY<48 and randint(1,50)==1:
        zombieOnScreen=False
        zombieHP=0
        infectStart=ticks

        
    #Change HP text color
    if HP>=50:
        HPr=0+5*(100-HP)
    else:
        HPr=255
    if HPr==255:
        HPg=255-5*(50-HP)

    #Move and draw enemy1
    if enemy1OnScreen:
        if enemy1X<guyX:
            enemy1X+=2
        if enemy1X>guyX:
            enemy1X-=2
        if enemy1Y<guyY:
            enemy1Y+=2
        if enemy1Y>guyY:
            enemy1Y-=2
        window.blit(enemy1, (enemy1X, enemy1Y))
    #Move and draw enemy2
    if enemy2OnScreen:
        if enemy2X<guyX:
            enemy2X+=1
        elif enemy2X>guyX:
            enemy2X-=1
        if enemy2Y<guyY:
            enemy2Y+=1
        elif enemy2Y>guyY:
            enemy2Y-=1
        window.blit(enemy2, (enemy2X, enemy2Y))
    #Move and draw Zombie
    if zombieOnScreen:
        if zombieX<guyX:
            zombieX+=randint(1,4)
        elif zombieX>guyX:
            zombieX-=randint(1,4)
        if zombieY<guyY:
            zombieY+=randint(1,4)
        elif zombieY>guyY:
            zombieY-=randint(1,4)
        window.blit(zombie, (zombieX, zombieY))

    #Damage enemy2 and check if dead
    if enemy1OnScreen and enemy2OnScreen and enemy1X-enemy2X<32 and enemy1X-enemy2X>-32 and enemy2Y-enemy1Y>-32 and enemy2Y-enemy1Y<32:
        enemy2HP-=0.2
        if ticks-damageStart<500:
            enemy2HP-=0.2
        window.blit(enemy2damaged, (enemy2X,enemy2Y))
        if enemy2HP<=0:
            playSound(440, 50)
            enemy2OnScreen=False
            coins+=25
            enemy2HP=0
            score+=500

    #Check if enemy1 is dead
    if enemy1OnScreen and enemy1HP<=0:
        playSound(396, 50)
        enemy1OnScreen=False
        coins+=10
        enemy1HP=0
        score+=250
    #Damage zombie with Double Damage
    if ticks-damageStart<500:
        zombieStart-=1
    #Check if zombie epidemic has gone away
    if zombieOnScreen and ticks-zombieStart>2500:
        playSound(412.5, 50)
        zombieOnScreen=False
        zombieHP=0
        coins+=30
        score+=750

    #Regen HP
    if HP<100-regenSpeed:
        HP+=regenSpeed
    else:
        HP=100

    #Open Chest
    if chestOnScreen and chestX-guyX<48 and chestX-guyX>-100 and guyY-chestY>-48 and guyY-chestY<60:
        playSound(165, 50)
        chestOnScreen=False
        window.blit(chestOpened, (chestX-15,chestY))
        pygame.display.update()
        coins+=randint(10,50)
        score+=10*randint(10,100)
        pygame.time.delay(500)
        
    # Update the screen
    pygame.display.update()

    #Check if level has advanced
    if score>=15000:
        level2()
    # Check for key presses
    for event in pygame.event.get():
        if (event.type==KEYUP and event.key==K_ESCAPE)or event.type==QUIT:
            done()
        
        # Check if an arrow key is pressed and 
        # move guy in the correct direction
        elif event.type==KEYDOWN:
            if ticks-speedStart<500:
                speed=baseSpeed*2
            else:
                speed=baseSpeed

            if event.key==K_w:
                if guyY>1:
                    guyY-=speed

            elif event.key==K_s:
                if guyY<652:
                    guyY+=speed

            elif event.key==K_a:
                if guyX>1:
                    guyX-=speed

            elif event.key==K_d:
                if guyX<1255:
                    guyX+=speed

            elif event.key==K_EQUALS:#DEVELOPER ONLY!
                coins+=10
                score+=100
                
                    
            elif event.key==K_1:
                if baseSpeed>=5.999:
                    drawText("ALREADY AT MAXIMUM VELOCITY!", 24, (255, 0, 0),650,680)
                    pygame.display.update()

                elif coins<baseSpeed*baseSpeed*baseSpeed:
                    drawText("NOT ENOUGH COINS! Cost: "+str(baseSpeed*baseSpeed*baseSpeed), 24, (255, 127,0),650,680)
                    pygame.display.update()
                        
                else:
                    drawText("Confirm Purchase \"SPEED +1\" for "+str(baseSpeed*baseSpeed*baseSpeed)+" Coins? ENTER/BACKSPACE", 20, (0, 0, 255),650,680)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type==KEYDOWN:
                            while not(event.type==KEYDOWN and (event.key==K_RETURN or event.key==K_BACKSPACE)):
                                for event in pygame.event.get():
                                    if event.type==KEYDOWN:
                                        if event.key==K_RETURN:
                                            playSound(206.25, 50)
                                            coins-=baseSpeed*baseSpeed*baseSpeed
                                            baseSpeed+=1
                                        elif event.key==K_BACKSPACE:
                                            break

            elif event.key==K_2:                       
                if regenSpeed>=0.005999:
                    drawText("ALREADY AT MAXIMUM HP REGEN SPEED!", 24, (255, 0, 0),650,680)
                    pygame.display.update()

                elif coins<int(1000*regenSpeed*1000*regenSpeed*1000*regenSpeed):
                    drawText("NOT ENOUGH COINS! Cost: "+str(int(1000*regenSpeed*1000*regenSpeed*1000*regenSpeed)), 24, (255, 127,0),650,680)
                    pygame.display.update()
                    
                else:
                    drawText("Confirm Purchase \"HP REGEN SPEED +1\" for "+str(int(1000*regenSpeed*1000*regenSpeed*1000*regenSpeed))+" Coins? RETURN/BACKSPACE", 19, (255, 0, 255),650,680)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type==KEYDOWN:
                            while not(event.type==KEYDOWN and (event.key==K_RETURN or event.key==K_BACKSPACE)):
                                for event in pygame.event.get():
                                    if event.type==KEYDOWN:
                                        if event.key==K_RETURN:
                                            playSound(198, 50)
                                            coins-=int(1000*regenSpeed*1000*regenSpeed*1000*regenSpeed)
                                            regenSpeed+=0.001
                                        elif event.key==K_BACKSPACE:
                                            break

        elif event.type==KEYUP:
                if event.key==K_SPACE:
                    if enemy1OnScreen and enemy1X-guyX<48 and enemy1X-guyX>-32 and guyY-enemy1Y>-48 and guyY-enemy1Y<32:
                        enemy1HP-=1
                        if ticks-damageStart<500:
                            enemy1HP-=1
                        window.blit(enemy1damaged, (enemy1X,enemy1Y))
                        pygame.display.update()
                        pygame.time.delay(100)
                   
for size in range(1,120):
    pygame.time.delay(2)
    drawText("GAME OVER!", size, (randint(0,255), randint(0,255), randint(0,255)),650,350)
    pygame.display.update()
drawText("GAME OVER!", 120, (255,0,0),650,350)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if (event.type==KEYUP and event.key==K_ESCAPE) or event.type==QUIT:
            pygame.quit()
            sys.exit(0)
