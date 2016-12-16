import pygame, sys
from pygame.locals import *
from array import array
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

pre_init(44100, -16, 1, 1024)    
pygame.init()
window = pygame.display.set_mode((1300,700), pygame.FULLSCREEN)
pygame.display.set_caption("Piano", "Piano")
BACKGROUND   = (127, 127, 127)                          #BACKGROUND
WHITE        = (255, 255, 255)                          #WHITE KEYS
BLACK        = (0  , 0  , 0  )                          #BLACK KEYS
baseHz       = 220                                      #KEY

sounds = {} 
keymap = { 
    pygame.K_z: baseHz, 
    pygame.K_s: baseHz*25/24,
    pygame.K_x: baseHz*9/8,
    pygame.K_d: baseHz*6/5,
    pygame.K_c: baseHz*5/4,
    pygame.K_v: baseHz*4/3,
    pygame.K_g: baseHz*45/32,
    pygame.K_b: baseHz*3/2,
    pygame.K_h: baseHz*8/5,
    pygame.K_n: baseHz*5/3,
    pygame.K_j: baseHz*9/5,
    pygame.K_m: baseHz*15/8,
    pygame.K_COMMA: baseHz*2
} 
while True:
    window.fill(BACKGROUND)
    for keyX in range(125,1225,150):
        pygame.draw.line(window, WHITE, (keyX,50), (keyX,550), 145)
    pygame.draw.line(window, BLACK, (200,50), (200,375), 60)
    pygame.draw.line(window, BLACK, (350,50), (350,375), 60)
    pygame.draw.line(window, BLACK, (650,50), (650,375), 60)
    pygame.draw.line(window, BLACK, (800,50), (800,375), 60)
    pygame.draw.line(window, BLACK, (950,50), (950,375), 60)
    pygame.display.update()

    evt = pygame.event.wait() 
    if evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == K_ESCAPE):
        pygame.quit()
        sys.exit(0)
    elif evt.type == pygame.KEYDOWN: 
        if evt.key in keymap: 
            note = Note(keymap[evt.key]) 
            note.play(-1)
            sounds[evt.key] = note
            
    elif evt.type == pygame.KEYUP:
        if evt.key in sounds:
            sounds.pop(evt.key).stop()
        if evt.key == K_EQUALS:
            baseHz *= 25/24
            keymap = { 
                pygame.K_z: baseHz, 
                pygame.K_s: baseHz*25/24,
                pygame.K_x: baseHz*9/8,
                pygame.K_d: baseHz*6/5,
                pygame.K_c: baseHz*5/4,
                pygame.K_v: baseHz*4/3,
                pygame.K_g: baseHz*45/32,
                pygame.K_b: baseHz*3/2,
                pygame.K_h: baseHz*8/5,
                pygame.K_n: baseHz*5/3,
                pygame.K_j: baseHz*9/5,
                pygame.K_m: baseHz*15/8,
                pygame.K_COMMA: baseHz*2
            } 
        if evt.key == K_MINUS:
            baseHz *= 24/25
            keymap = { 
                pygame.K_z: baseHz, 
                pygame.K_s: baseHz*25/24,
                pygame.K_x: baseHz*9/8,
                pygame.K_d: baseHz*6/5,
                pygame.K_c: baseHz*5/4,
                pygame.K_v: baseHz*4/3,
                pygame.K_g: baseHz*45/32,
                pygame.K_b: baseHz*3/2,
                pygame.K_h: baseHz*8/5,
                pygame.K_n: baseHz*5/3,
                pygame.K_j: baseHz*9/5,
                pygame.K_m: baseHz*15/8,
                pygame.K_COMMA: baseHz*2
            } 
