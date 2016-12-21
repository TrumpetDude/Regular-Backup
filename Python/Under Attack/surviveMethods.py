from array import array
from time import sleep
from random import randint
import pygame, sys
from pygame.locals import *
from pygame.mixer import Sound, get_init, pre_init

    
class Note(Sound):

    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

if __name__ == "__main__":
    pre_init(44100, -16, 1, 1024)
    pygame.init()
    Note(440).play(-1)
    sleep(5)

def drawText(window, text, size, color, centerX, centerY):
    font=pygame.font.Font("PressStart2P.ttf", size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

def drawAlways(window, score, coins, HP, HPr, HPg, enemy1OnScreen, enemy1HP, enemy2OnScreen, enemy2HP, zombieOnScreen, zombieHP):
    window.fill((0,0,0))
    pygame.draw.rect(window, (50,50,50), (0,0,315,50),0)
    pygame.draw.line(window,(0,0,0) ,(125,0), (125,50), 5)
    drawText(window, "+ SPEED: 1",12,(0, 0, 255),50,25)
    drawText(window, "+ HP REGEN: 2",12,(255, 0, 255),220,25)
    drawText(window, "COINS: "+str(coins), 26, (255,255,0),650,20)
    drawText(window, "HP: "+str(int(HP//1)), 26, (HPr, HPg, 0),650,50)
    drawText(window, "SCORE: "+str(score), 26, (255,255,255),1100,20)
    if enemy1OnScreen or enemy2OnScreen or zombieOnScreen:
        drawText(window, "TOTAL ENEMY HP: "+str(int(enemy1HP//1)+int(enemy2HP//1)+int(zombieHP//1)), 26, (255,0,0),650,80)
        
def regenHP(HP, regenSpeed):
    if HP<100-regenSpeed:
        HP+=regenSpeed
    else:
        HP=100
    return HP

def level2(window):
    pygame.draw.line(window,(50,50,50),(0,350),(1300,350),200)
    drawText(window, "You have completed Level 1!",20,(200,200,200),650,300)
    drawText(window, "Continue",24,(200,200,200),650,400)
    pygame.draw.rect(window, (200,200,200), (540,375,220,50), 5)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYUP and event.key == K_ESCAPE):
                done(window)
        mousePos=pygame.mouse.get_pos()
        mousePressed=pygame.mouse.get_pressed()
        if mousePos[1]>375 and mousePos[1]<425 and mousePos[0]>540 and mousePos[0]<760 and (mousePressed[0] or mousePressed[1] or mousePressed[2]):
            import zombieApocalypse

def done(window):
    pygame.draw.line(window,(50,50,50),(0,350),(1300,350),200)
    drawText(window, "Are you sure you want to quit? Your Progress will not be saved.",20,(200,200,200),650,300)
    drawText(window, "Yes               No",24,(200,200,200),650,400)
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

def gameOver(window):
    for size in range(1,120):
        pygame.time.delay(2)
        drawText(window, "GAME OVER!", size, (randint(0,255), randint(0,255), randint(0,255)),650,350)
        pygame.display.update()
    drawText(window, "GAME OVER!", 120, (255,0,0),650,350)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if (event.type==KEYUP and event.key==K_ESCAPE) or event.type==QUIT:
                pygame.quit()
                sys.exit(0)

def playSound(hz,ms):
    pre_init(44100, -16, 1, 1024)
    Note(hz).play(ms)

def drawStuff(window, coinOnScreen, coinX, coinY, chest, chestOnScreen, chestX, chestY):
    if coinOnScreen:
        pygame.draw.circle(window, (255,255,0),(coinX,coinY),8,0)
    if chestOnScreen:
        window.blit(chest, (chestX, chestY))
