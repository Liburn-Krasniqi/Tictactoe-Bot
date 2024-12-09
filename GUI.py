"""
pygame HAS to be imported and used in a virtual env 
"""
import pygame

pygame.init()

"""
display values
"""
size = 600

screen = pygame.display.set_mode((size, size))

width = screen.get_width() 
height = screen.get_height() 

#  positions array for coords in the grid (to place Xs and Os)
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
playXButton = pygame.Rect(width/2+width/8, height/2+30, 140, 50)
playasx = smallfont.render('Play as X', True, white)
playXRect = playasx.get_rect()
playXRect.center = playXButton.center

playOButton = pygame.Rect(width/2-width/8-140, height/2+30, 140, 50)
playaso = smallfont.render('Play as O', True, white)
playORect = playaso.get_rect()
playORect.center = playOButton.center

gameName = bigfont.render('TICTACTOE', True, white)
gameNameRect = gameName.get_rect()
gameNameRect.center = (width/2, 200)


X = playFont.render('X', True, white)
O = playFont.render('O', True, white)

"""
whatever 
"""

fontHeight = playFont.get_height()
xWidth = playFont.size("X")[0]
oWidth = playFont.size("O")[0]

player = None

smth = False  # temp value not used for anything specific other than a code tool

run = True  

while run:

    screen.fill((black))  # dark backdrop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pos() 

    #  draw Start(?) Screen

    if player == None:
        screen.blit(gameName, gameNameRect) 

        pygame.draw.rect(screen, color_dark, playXButton)
        screen.blit(playasx, playXRect) 

        pygame.draw.rect(screen, color_dark, playOButton)
        screen.blit(playaso, playORect) 

        if playXButton.collidepoint(mouse):
            pygame.draw.rect(screen, color_light, playXButton)
            screen.blit(playasx, playXRect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                player = X  
        elif playOButton.collidepoint(mouse):
            pygame.draw.rect(screen, color_light, playOButton)
            screen.blit(playaso, playORect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                player = O  
    else:
        #  Draw the Grid H-horizontal line V-vertical line
        pygame.draw.line(screen, white, [width/8, height/3+20], [width-width/8, height/3+20], 1)  # H 1
        pygame.draw.line(screen, white, [width/3+20, height/8], [width/3+20, height-height/8], 1) # V 1
        pygame.draw.line(screen, white, [width/8, height-height/3-20], [width-width/8, height-height/3-20], 1)  # H 2
        pygame.draw.line(screen, white, [width-width/3-20, height/8], [width-width/3-20, height-height/8], 1)  # V 2
        
# position x
    # if smth==False and player != None and width/3+20 <= mouse[0] <= (width-width/3-20) and height/3+20 <= mouse[1] <= (height-height/3-20):
    #     pygame.draw.rect(screen, color_dark, [width/3+20, height/3+20, 160, 160])
    # if smth == True:   
    #     screen.blit(O, (positionsX[1]-oWidth/2, positionsY[1]-fontHeight/2)) 

    pygame.display.update()


pygame.quit()