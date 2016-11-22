'''
TO-DO:
Mrs. Maudie's House
Jail
Meridian Highway
Bushes
Stephanie Crawford's House
Extra Buildings in Square
'''
import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
window = pygame.display.set_mode((1300,700))
pygame.key.set_repeat(1,1)
BLACK=(0,0,0)
WHITE=(255,255,255)
BACKGROUND=(180,160,120)
ROAD=(80,30,10)
view="SQUARE"
news=pygame.image.load("news.gif")
#Credit: https://pixabay.com/en/news-newspaper-article-147716/
court=pygame.image.load("gavel.gif")
#Credit: http://humbliceous.blogspot.com/2006/01/gavel.html
house=pygame.image.load("house.gif")
#Credit: https://pt.wikipedia.org/wiki/Ficheiro:House.png
smallHouse=pygame.image.load("smallHouse.gif")
#Credit: https://pt.wikipedia.org/wiki/Ficheiro:House.png
radley=pygame.image.load("boo.gif")
#Credit: http://www.freestockphotos.biz/stockphoto/12056
dubose=pygame.image.load("frowny.gif")
#Credit: https://en.wikipedia.org/wiki/File:Angry_face.png

def drawText(text, size, color, fontName, centerX, centerY):
    font=pygame.font.SysFont(fontName, size)
    renderedText=font.render(text,True,(0,0,0))
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

'''
Notes on Maycomb County:
Page 6: "In rainy weather the streets turned to red slop; grass grew on the sidewalks, the courthouse sagged in the square."
Page 6: "We lived on the main residential street in town."
Page 7: "Mrs. Henry Lafayette Dubose's house two doors to the north of us, and the Radley Place three doors to the south."
Page 199-200: "We went by Mrs. Dubose's house...there were 8 more houses to the post office corner."
Page 200: "Giant Monkey-puzzle bushes bristled on each corner, and between them an iron hitching rail glistened under under the street lights."
Page 200: "Atticus's office was in the courthouse when he began his law practice. but after several years of it he moved to quieter quarters in the Maycomb Bank Building.
Page 200: "Mr Underwood...lived above [The Maycomb Tribune office]...The office building was on the northwest corner of the square, and to reach it we had to pass the jail."
Page 201: "...cars came in from the Meridian Highway, moving slowly in a line. They went around the square, passed the bank building, and stopped in front of the jail."
'''
while True:
    
    mousePos=pygame.mouse.get_pos()
    mousePressed=pygame.mouse.get_pressed()
    window.fill(BACKGROUND)

    if view=="SQUARE":
        #Squares, down label, spacefiller house
        pygame.draw.line(window, ROAD, (400,100), (900,100), 50)
        pygame.draw.line(window, ROAD, (400,76), (400,626), 50)
        pygame.draw.line(window, ROAD, (376,601), (900,601), 50)
        pygame.draw.line(window, ROAD, (900,76), (900,626), 50)
        pygame.draw.line(window, ROAD, (650,600), (650,700), 50)
        drawText("DOWN", 14, BLACK, "comicsansms", 650, 660)
        window.blit(smallHouse, (580,662))
        #Maycomb County Tribune
        window.blit(news, (300,0))
        if mousePos[1]>0 and mousePos[1]<80 and mousePos[0]>310 and mousePos[0]<390:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Maycomb Tribune..........Page 200: \"The office building was on the northwest corner of the square...\"", 20, BLACK, "comicsansms", 650, 20)
        #Courthouse
        window.blit(court, (525,240))
        if mousePos[1]>240 and mousePos[1]<400 and mousePos[0]>525 and mousePos[0]<752:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Caurthouse..........Page 6: \"...the courthouse sagged in the square.\"", 20, BLACK, "comicsansms", 650, 20)
            
    if view=="HOUSES":
        #Road, up label, spacefiller houses
        pygame.draw.line(window, ROAD, (650,0),  (650,700), 50)
        drawText("UP", 20, WHITE, "comicsansms", 650, 30)
        for y in range(2,300,40):
            window.blit(smallHouse, (580,y))
        window.blit(smallHouse, (580,365))
        window.blit(smallHouse, (580,490))
        window.blit(smallHouse, (580,530))
        for y in range(2,680,40):
            window.blit(smallHouse, (680,y))
        #Ms. Dubose's House
        window.blit(dubose, (535,280))
        if mousePos[1]>280 and mousePos[1]<360 and mousePos[0]>535 and mousePos[0]<615:
            pygame.draw.line(window, WHITE, (0,39), (1300,39), 80)
            drawText("Ms. Dubose's House..........Page 7: \"Mrs. Henry Lafayette Dubose's house two doors to the north of us...\"", 20, BLACK, "comicsansms", 650, 20)
            drawText("Page 199-200: \"We went by Mrs. Dubose's house...there were 8 more houses to the post office corner.\"", 20, BLACK, "comicsansms", 650,55)
        #Scout's House
        window.blit(house, (550,410))
        if mousePos[1]>410 and mousePos[1]<474 and mousePos[0]>550 and mousePos[0]<614:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Scout's House..........Page 6: \"We lived on the main residential street in town.\"", 20, BLACK, "comicsansms", 650, 20)
        #Radley Place
        window.blit(radley, (520,560))
        if mousePos[1]>560 and mousePos[1]<685 and mousePos[0]>530 and mousePos[0]<610:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Radley Place..........Page 7: \"...the Radley Place three doors to the south.\"", 20, BLACK, "comicsansms", 650, 20)
        
    pygame.display.update()
    
    for event in pygame.event.get():
        if (event.type==KEYUP and event.key==K_ESCAPE) or event.type==QUIT:
            pygame.quit()
            sys.exit()
            
    #Change view
    if mousePos[1]>626 and mousePos[1]<700 and mousePos[0]>626 and mousePos[0]<676 and sum(mousePressed) and view=="SQUARE":
        view="HOUSES"
    if mousePos[1]>0 and mousePos[1]<74 and mousePos[0]>626 and mousePos[0]<676 and sum(mousePressed) and view=="HOUSES":
        view="SQUARE"
    
