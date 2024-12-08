"""
pygame HAS to be imported and used in a virtual env 
"""
import pygame

pygame.init()

"""
display values
"""
SCREEN_WIDTH=600
SCREEN_HEIGHT=600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

width = screen.get_width() 
height = screen.get_height() 

positionsX = [(width/5+20),(width/2),(width - (width/5+20))]
positionsY = [(height/5+20),(height/2),(height - (height/5+20))]


"""
color presets
"""
white = (255,255,255)

black = (0, 0, 0)

color_light = (170,170,170) 

color_dark = (100,100,100) 

red = (255, 0, 0)

"""
Font style presets
"""
smallfont = pygame.font.SysFont('Corbel',35) 

bigfont = pygame.font.SysFont('Corbel',55) 

playFont = pygame.font.SysFont('tahoma', 100, bold=False, italic=False)

"""
Game text
"""
playasx = smallfont.render('Play as X', True, white)

playaso = smallfont.render('Play as O', True, white)

gameName = bigfont.render('TICTACTOE', True, white)

X = playFont.render('X', True, white)
O = playFont.render('O', True, white)

"""
whatever 
"""

fontHeight = playFont.get_height()
xWidth = playFont.size("X")[0]
oWidth = playFont.size("O")[0]

xPlayer = False
oPlayer = False

smth = False

run = True  
while run:

    screen.fill((black))  # dark backdrop

    mouse = pygame.mouse.get_pos() 

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/3+20 <= mouse[0] <= (width-width/3-20) and height/3+20 <= mouse[1] <= (height-height/3-20):
                # char width can be made variable in a function and passed as an arg
                smth=True
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

    if xPlayer == False and oPlayer == False:
        screen.blit(gameName, (width/2-width/8-50, height/2-100)) 
    else:
        pygame.draw.line(screen, white, [width/8, height/3+20], [width-width/8, height/3+20], 1)  # H 1
        pygame.draw.line(screen, white, [width/3+20, height/8], [width/3+20, height-height/8], 1) # V 1

        pygame.draw.line(screen, white, [width/8, height-height/3-20], [width-width/8, height-height/3-20], 1)  # H 2
        pygame.draw.line(screen, red, [width-width/3-20, height/8], [width-width/3-20, height-height/8], 1)  # V 2

    if smth==False and xPlayer == True and width/3+20 <= mouse[0] <= (width-width/3-20) and height/3+20 <= mouse[1] <= (height-height/3-20):
        pygame.draw.rect(screen, color_dark, [width/3+20, height/3+20, 160, 160])
    if smth == True:   
        screen.blit(O, (positionsX[1]-oWidth/2, positionsY[1]-fontHeight/2)) 

    pygame.display.update()


pygame.quit()