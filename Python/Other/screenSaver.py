import pygame, sys
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
r = 0
g = 0
b = 0
for b in range(256):
        window.fill((r,g,b))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
while True:
    for r in range(256):
        window.fill((r,g,b))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
    for b in range(255,-1,-1):
        window.fill((r,g,b))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
    for g in range(256):
        window.fill((r,g,b))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
    for r in range(255,-1,-1):
        window.fill((r,g,b))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
    for b in range(256):
        window.fill((r,g,b))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
    for g in range(255,-1,-1):
        window.fill((r,g,b))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pygame.quit()
                sys.exit()
