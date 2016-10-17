import pygame

pygame.init()

while(1):
    keys=pygame.key.get_pressed()

    for event in pygame.event.get():
    # determin if X was clicked, or Ctrl+W or Alt+F4 was used 
        if (event.type == pygame.QUIT):
            print("Quit")
        
        if event.type == pygame.KEYDOWN:
            #
            if event.key == pygame.K_w and ctrl_held:
                print("cntrl")
            if event.key == pygame.K_F4 and alt_held:
                print("Alt")
            if event.key == pygame.K_ESCAPE:
                print("Escp")
                
            # determine if a letter key was pressed 
            if event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue'
