'''
Notes on Maycomb County:
Page 6: "In rainy weather the streets turned to red slop; grass grew on the sidewalks, the courthouse sagged in the square."
Page 6: "We lived on the main residential street in town."
Page 7: "Mrs. Henry Lafayette Dubose's house two doors to the north of us, and the Radley Place three doors to the south."
Page 93: Smoke was rolling off our house and Miss Rachel's house..."
Pages 199-200: "We went by Mrs. Dubose's house...there were 8 more houses to the post office corner."
Page 200: "Giant Monkey-puzzle bushes bristled on each corner, and between them an iron hitching rail glistened under under the street lights."
Page 200: "Mr Underwood...lived above [The Maycomb Tribune office]...The office building was on the northwest corner of the square, and to reach it we had to pass the jail."
Page 201: "...cars came in from the Meridian Highway, moving slowly in a line. They went around the square, passed the bank building, and stopped in front of the jail."
Page 227: "Maycomb's Ewells lived behind the town garbage dump in what was once a negro cabin."
Pages 228-229: "A dirt road ran from the highway past the dump, down to a small negro settlement some five hundrd yards beyond the Ewells'."
'''

import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((1300,700),pygame.FULLSCREEN)
pygame.display.set_caption("Maycomb County","Maycomb County")
pygame.key.set_repeat(1,1)
BLACK=(0,0,0)
GREY=(127,127,127)
WHITE=(255,255,255)
BACKGROUND=(180,160,120)
ROAD=(80,30,10)
DIRTROAD=(100,80,65)
view="SQUARE"

news=pygame.image.load("news.gif")
#Credit: https://pixabay.com/en/news-newspaper-article-147716/
court=pygame.image.load("gavel.gif")
#Credit: http://humbliceous.blogspot.com/2006/01/gavel.html
scout=pygame.image.load("house.gif")
#Credit: https://pt.wikipedia.org/wiki/Ficheiro:House.png
smallHouse=pygame.image.load("smallHouse.gif")
#Credit: https://pt.wikipedia.org/wiki/Ficheiro:House.png
radley=pygame.image.load("knothole.gif")
#Credit: http://www.publicdomainpictures.net/view-image.php?image=129276&picture=tree-knothole
dubose=pygame.image.load("frowny.gif")
#Credit: https://en.wikipedia.org/wiki/File:Angry_face.png
bush=pygame.image.load("bush.gif")
#Credit: https://pixabay.com/en/bush-shrub-green-nature-plant-576310/
jail=pygame.image.load("bars.gif")
#Credit: https://pixabay.com/en/photos/prison/
maudie=pygame.image.load("flower.gif")
#Credit: https://pixabay.com/en/flower-blossom-purple-plant-petals-305777/
rachel=pygame.image.load("mediumHouse.gif")
#Credit: https://pt.wikipedia.org/wiki/Ficheiro:House.png
church=pygame.image.load("church.gif")
#Credit: https://upload.wikimedia.org/wikipedia/commons/b/b4/Religion_08.svg
smallChurch=pygame.image.load("smallChurch.gif")
#Credit: https://upload.wikimedia.org/wikipedia/commons/b/b4/Religion_08.svg
outerVillage=pygame.image.load("outerVillage.gif")
#Credit: http://www.publicdomainpictures.net/view-image.php?image=79911&picture=trash-can-clip-art
#Credit: https://pixabay.com/en/loghut-hut-wooden-door-window-311659/

def drawText(text, size, color, fontName, centerX, centerY):
    font=pygame.font.SysFont(fontName, size)
    renderedText=font.render(text,True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)

while True:
    
    mousePos=pygame.mouse.get_pos()
    mousePressed=pygame.mouse.get_pressed()
    window.fill(BACKGROUND)

    if view=="SQUARE":
        #Roads, down label, spacefiller houses
        pygame.draw.line(window, ROAD, (400,100), (900,100), 50)
        pygame.draw.line(window, ROAD, (400,76), (400,626), 50)
        pygame.draw.line(window, ROAD, (376,601), (900,601), 50)
        pygame.draw.line(window, ROAD, (900,0), (900,626), 50)
        pygame.draw.line(window, ROAD, (650,600), (650,700), 50)
        pygame.draw.line(window, DIRTROAD, (900,627),(900,700),30)
        drawText("DOWN", 14, WHITE, "comicsansms", 650, 660)
        window.blit(smallHouse, (580,665))
        window.blit(smallHouse, (680,665))
        #Maycomb County Tribune
        window.blit(news, (305,1))
        if mousePos[1]>1 and mousePos[1]<81 and mousePos[0]>315 and mousePos[0]<375:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Maycomb Tribune..........Page 200: \"The office building was on the northwest corner of the square...\"", 20, BLACK, "comicsansms", 650, 20)
        #Courthouse
        window.blit(court, (535,260))
        if mousePos[1]>260 and mousePos[1]<420 and mousePos[0]>525 and mousePos[0]<762:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Courthouse..........Page 6: \"...the courthouse sagged in the square.\"", 20, BLACK, "comicsansms", 650, 20)
        #Church
        window.blit(church, (920,300))
        if mousePos[1]>260 and mousePos[1]<420 and mousePos[0]>525 and mousePos[0]<762:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Courthouse..........Page 6: \"...the courthouse sagged in the square.\"", 20, BLACK, "comicsansms", 650, 20)
        #Monkey-Puzzle Bushes and Hitching Rails
        pygame.draw.line(window,GREY, (480,145), (820,145), 20)
        pygame.draw.line(window,GREY, (445,145), (445,560), 20)
        pygame.draw.line(window,GREY, (855,145), (855,560), 20)
        pygame.draw.line(window,GREY, (480,557), (820,557), 20)
        window.blit(bush, (426,126))
        window.blit(bush, (426,530))
        window.blit(bush, (796,126))
        window.blit(bush, (796,530))
        if mousePos[1]>126 and mousePos[1]<173 and mousePos[0]>426 and mousePos[0]<506 or mousePos[1]>126 and mousePos[1]<173 and mousePos[0]>796 and mousePos[0]<876 or mousePos[1]>530 and mousePos[1]<577 and mousePos[0]>426 and mousePos[0]<506 or mousePos[1]>530 and mousePos[1]<577 and mousePos[0]>796 and mousePos[0]<876:
            pygame.draw.line(window, WHITE, (0,39), (1300,39), 80)
            drawText("Bushes and Rail..........Page 200: \"Giant Monkey-puzzle bushes bristled on each corner, ", 20, BLACK, "comicsansms", 650, 20)
            drawText("and between them an iron hitching rail glistened under under the street lights.\"", 20, BLACK, "comicsansms", 650,55)
        #Bank
        drawText("$", 80, BLACK, "consolas", 750, 668)
        if mousePos[1]>628 and mousePos[1]<698 and mousePos[0]>730 and mousePos[0]<770:
            pygame.draw.line(window, WHITE, (0,39), (1300,39), 80)
            drawText("Bank..........Page 201: \"...cars came in from the Meridian Highway, moving slowly in a line.", 20, BLACK, "comicsansms", 650, 20)
            drawText("They went around the square, passed the bank building, and stopped in front of the jail.\"", 20, BLACK, "comicsansms", 650,55)
        #Jail
        window.blit(jail,(296,620))
        if mousePos[1]>620 and mousePos[1]<694 and mousePos[0]>296 and mousePos[0]<376:
            pygame.draw.line(window, WHITE, (0,39), (1300,39), 80)
            drawText("Maycomb County Jail..........Page 200: \"...to reach [the Maycomb Tribune office building] we had to pass the jail.\"", 20, BLACK, "comicsansms", 650, 20)
            drawText("Page 201: \"[The Cars] went around the square, passed the bank building, and stopped in front of the jail.\"", 20, BLACK, "comicsansms", 650,55)
            
    if view=="HOUSES":
        #Road, up label, spacefiller houses
        pygame.draw.line(window, ROAD, (650,0),  (650,700), 50)
        pygame.draw.line(window, DIRTROAD, (900,0), (900,350), 30)
        pygame.draw.line(window, DIRTROAD, (900,335), (1150,335), 30)
        drawText("UP", 20, WHITE, "comicsansms", 650, 30)
        for y in range(0,225,35):
            window.blit(smallHouse, (580,y))
        window.blit(smallHouse, (580,335))
        for y in range(0,700,35):
            window.blit(smallHouse, (680,y))
        #Ms. Dubose's House
        window.blit(dubose, (535,250))
        if mousePos[1]>250 and mousePos[1]<330 and mousePos[0]>535 and mousePos[0]<615:
            pygame.draw.line(window, WHITE, (0,39), (1300,39), 80)
            drawText("Ms. Dubose's House..........Page 7: \"Mrs. Henry Lafayette Dubose's house two doors to the north of us...\"", 20, BLACK, "comicsansms", 650, 20)
            drawText("Page 199-200: \"We went by Mrs. Dubose's house...there were 8 more houses to the post office corner.\"", 20, BLACK, "comicsansms", 650,55)
        #Scout's House
        window.blit(scout, (550,375))
        if mousePos[1]>375 and mousePos[1]<439 and mousePos[0]>550 and mousePos[0]<614:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Scout's House..........Page 6: \"We lived on the main residential street in town.\"", 20, BLACK, "comicsansms", 650, 20)
        #Miss Maudie's House
        window.blit(maudie, (540,450))
        if mousePos[1]>450 and mousePos[1]<529 and mousePos[0]>540 and mousePos[0]<620:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Miss Maudie's House..........Page 93: \"Smoke was rolling off our house and Miss Rachel's house...\"", 20, BLACK, "comicsansms", 650, 20)
        #Miss Rachel's House
        window.blit(rachel, (560,535))
        if mousePos[1]>535 and mousePos[1]<583 and mousePos[0]>560 and mousePos[0]<640:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Miss Rachel's House..........Page 93: \"Smoke was rolling off our house and Miss Rachel's house...\"", 20, BLACK, "comicsansms", 650, 20)
        #Radley Place
        window.blit(radley, (540,590))
        if mousePos[1]>590 and mousePos[1]<690 and mousePos[0]>535 and mousePos[0]<614:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Radley Place..........Page 7: \"...the Radley Place three doors to the south.\"", 20, BLACK, "comicsansms", 650, 20)
        #Dump, Ewell house, Black Community, and First Purchase
        window.blit(outerVillage, (718,200))
        window.blit(smallChurch, (1185,305))
        if mousePos[1]>230 and mousePos[1]<320 and mousePos[0]>795 and mousePos[0]<1020:
            pygame.draw.line(window, WHITE, (0,23), (1300,23), 48)
            drawText("Dump and Ewells' House..........Page 227: \"Maycomb's Ewells lived behind the town garbage dump in what was once a negro cabin.\"", 20, BLACK, "comicsansms", 650, 20)
        if mousePos[1]>290 and mousePos[1]<400 and mousePos[0]>1150 and mousePos[0]<1290:
            pygame.draw.line(window, WHITE, (0,39), (1300,39), 80)
            drawText("Black Community and First Purchase..........Pages 228-229: \"A dirt road ran from the highway past the dump,", 20, BLACK, "comicsansms", 650, 20)
            drawText("down to a small negro settlement some five hundrd yards beyond the Ewells'.\"", 20, BLACK, "comicsansms", 650,55)
        
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
