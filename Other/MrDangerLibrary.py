#My "Library" for python and pygame
#Contains methods that I use in my programs

#SAMPLE CODE, IMPORTING WONT WORK
def drawTextFF(text, size, color, centerX, centerY):
    font=pygame.font.Font("yourFontFile.ttf or None", size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

#MAKE SURE FONT IS INSTALLED ON YOUR SYSTEM 
def drawTextSysF(text, size, color, fontName, centerX, centerY):
    font=pygame.font.SysFont(fontName, size)
    renderedText=font.render(text,True,(0,0,0))
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

def pygameInit(xDim, yDim, caption, minimizedCaption, firstRepeat, constantRepeat):
    import pygame
    from pygame.locals import *
    pygame.init()
    window=pygame.display.set_mode((xDim,yDim))
    pygame.display.set_caption(caption,minimizedCaption)
    pygame.key.set_repeat(firstRepeat,constantRepeat)

def importCommonLibs():
    import random
    from random import randint
    import time
    from time import sleep
    import sys

