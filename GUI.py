"""
pygame HAS to be imported and used in a virtual env 
"""
import pygame
import time
import ai as game
pygame.init()
pygame.display.set_caption("Tic-tac-toe")
"""
display values
"""
size = 600

screen = pygame.display.set_mode((size, size))

width = screen.get_width() 
height = screen.get_height() 

# positions array for coords in the grid (to place Xs and Os)
# positionsX = [(width/5+20),(width/2),(width - (width/5+20))]
# positionsY = [(height/5+20),(height/2),(height - (height/5+20))]


"""
color presets
"""
white = (255, 255, 255)

black = (0, 0, 0)

color_light = (170, 170, 170) 

color_dark = (100, 100, 100) 

"""
Font style presets
"""
smallfont = pygame.font.SysFont('Corbel', 35) 

bigfont = pygame.font.SysFont('Corbel', 55) 

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

"""
whatever 
"""
user = None
board = game.initial_state()

ai_turn = False  

run = True  

    
while run:

    game_over = game.terminal(board)
    player = game.player(board)

    screen.fill((black))  # dark backdrop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pos() 

    #  draw Start(?) Screen
    if user == None:
        screen.blit(gameName, gameNameRect) 

        pygame.draw.rect(screen, color_dark, playXButton)
        screen.blit(playasx, playXRect) 

        pygame.draw.rect(screen, color_dark, playOButton)
        screen.blit(playaso, playORect) 

        if playXButton.collidepoint(mouse):
            pygame.draw.rect(screen, color_light, playXButton)
            screen.blit(playasx, playXRect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                time.sleep(0.2)  # so our event doesnt carry to the next step
                user = game.X  
        elif playOButton.collidepoint(mouse):
            pygame.draw.rect(screen, color_light, playOButton)
            screen.blit(playaso, playORect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                time.sleep(0.2)
                user = game.O  
                ai_turn = True
    else:
        #  Draw the Grid; H-horizontal line V-vertical line
        pygame.draw.line(screen, white, [width/8, height/3+20],
                         [width-width/8, height/3+20], 1)  # H 1

        pygame.draw.line(screen, white, [width/3+20, height/8],
                         [width/3+20, height-height/8], 1)  # V 1
        
        pygame.draw.line(screen, white,
                         [width/8, height-height/3-20], [width-width/8, height-height/3-20], 1)  # H 2
        
        pygame.draw.line(screen, white,
                         [width-width/3-20, height/8], [width-width/3-20, height-height/8], 1)  # V 2

        # this is to set the tile space (like for the mouse type shit ...god I dont know how to speak)
        tile_size = 160
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []  
        
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                if board[i][j] != game.EMPTY:
                    move = playFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        # Show title
        if game_over:
            winner = game.winner(board)
            if winner is None:
                title = "Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."       
        elif user == player:
            title = f"Play as {user}"
        else:
            title = "Computer thinking..."
        title = bigfont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect) 

        # ai turn 
        if user != player and not game_over:
            if ai_turn:
                pygame.display.update()  # i did not know how else to fix this (will look into it l8r)
                move = game.minimax(board)
                board = game.result(board, move)
                time.sleep(1)
                ai_turn = False
    
        # user turn
        for i in range(3): 
            for j in range(3):
                if tiles[i][j].collidepoint(mouse) and board[i][j] == game.EMPTY and game.terminal(board) != True:
                    pygame.draw.rect(screen, color_dark, [(tiles[i][j])[0],
                                                          (tiles[i][j])[1], 160, 160])
                    if event.type == pygame.MOUSEBUTTONDOWN and game.terminal(board) != True:
                        time.sleep(0.2)
                        board = game.result(board, (i, j))
                        ai_turn = True
           
    pygame.display.update()


pygame.quit()