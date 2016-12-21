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

def drawAlways(window, score, HP, HPr, HPg, zombies):
    window.fill((0,0,0))
    drawText(window, "HP: "+str(int(HP//1)), 26, (HPr, HPg, 0),650,20)
    drawText(window, "SCORE: "+str(score), 26, (50,150,50),1100,20)
    drawText(window, "ZOMBIES: "+str(len(zombies)), 26, (255,0,0),650,50)

def regenHP(HP, regenSpeed):
    if HP<100-regenSpeed:
        HP+=regenSpeed
    else:
        HP=100
    return HP

def done(window):
    pygame.draw.line(window,(25,75,25),(0,350),(1300,350),200)
    drawText(window, "Are you sure you want to quit? Your Progress will not be saved.",20,(120,200,120),650,300)
    drawText(window, "Yes               No",24,(120,200,120),650,400)
    pygame.draw.rect(window, (120,200,120), (395,375,100,50), 5)
    pygame.draw.rect(window, (120,200,120), (815,375,100,50), 5)
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
        drawText(window, "GAME OVER!", size, (0, size*2, 0),650,350)
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
