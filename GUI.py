import pygame

pygame.init()

SCREEN_WIDTH=600
SCREEN_HEIGHT=600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 25, 25))

color = (255,255,255)

color_light = (170,170,170) 

color_dark = (100,100,100) 

smallfont = pygame.font.SysFont('Corbel',35) 

bigfont = pygame.font.SysFont('Corbel',55) 

playasx = smallfont.render('Play as X' , True , color)

playaso = smallfont.render('Play as O' , True , color)

text2 = bigfont.render('TICTACTOE' , True , color)

xPlayer = False
oPlayer = False

width = screen.get_width() 
height = screen.get_height() 

run = True  
while run:

    screen.fill((0,0,0))

    mouse = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2+width/8 <= mouse[0] <= width/2+width/8+140 and height/2+30 <= mouse[1] <= height/2+30+50: 
                xPlayer = True
        if event.type == pygame.QUIT:
            run = False

    if xPlayer == False and oPlayer == False and width/2+width/8 <= mouse[0] <= width/2+width/8+140 and height/2+30 <= mouse[1] <= height/2+30+50:
        pygame.draw.rect(screen, color_light, [width/2+width/8, height/2+30, 140, 50])
        screen.blit(playasx, (width/2+width/8+10,height/2+40)) 
    elif xPlayer == False and oPlayer == False:
        pygame.draw.rect(screen, color_dark, [width/2+width/8, height/2+30, 140, 50])
        screen.blit(playasx, (width/2+width/8+10,height/2+40)) 

    if xPlayer == False and oPlayer == False and width/2-width/8-140 <= mouse[0] <= width/2-width/8 and height/2+30 <= mouse[1] <= height/2+30+50:
        pygame.draw.rect(screen, color_light, [width/2-width/8-140, height/2+30, 140, 50])
        screen.blit(playaso, (width/2-width/8-132,height/2+40))
    elif xPlayer == False and oPlayer == False:
        pygame.draw.rect(screen, color_dark, [width/2-width/8-140, height/2+30, 140, 50])
        screen.blit(playaso, (width/2-width/8-132,height/2+40))

    screen.blit(text2, (width/2-width/8-50, height/2-100)) 

    pygame.display.update()
pygame.quit()