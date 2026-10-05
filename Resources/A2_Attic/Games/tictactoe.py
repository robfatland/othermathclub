import pygame         # gives us a nice game board to draw on
import time           # gives us the ability to put in little pauses
import random         # used to choose computer's moves

# Based on the board[] list this draws all the Xs and Os
def DrawBoard():
    global board
    for i in range(9):
        if board[i] == 'x':
            x = square * (i%3)
            y = square * int(i/3)
            pygame.draw.line(screen, white, (x + 20, y + 20), (x + 180, y + 180), 2)
            pygame.draw.line(screen, white, (x + 180, y + 20), (x + 20, y + 180), 2)
        elif board[i] == 'o':
            x = square * (i%3)
            y = square * int(i/3)
            pygame.draw.circle(screen, white, (x + 100, y + 100), 80, 2)
    pygame.display.flip()

# Selects a move for the computer (but does not draw it)
def MyMove():
    global board
    p = []
    for i in range(9):
        if board[i] == ' ': p.append(i)
    if len(p) > 0:
        m = random.randint(0, len(p)-1)
        board[p[m]] = 'o'
    return

# Determines if the game is over and if so: Was it a tie or did someone win?
#   Notice that it returns two logical values; for example (True, False). The first of
#   these is whether the game is over; and the second one is whether the game was a tie.
#   Notice that it is logically impossible to return (False, True)
def GameOver():
    global board

    # Check for a win across rows
    for i in range(0, 3):
        if (board[0 + 3*i] == 'x' and board[1 + 3*i] == 'x' and board[2 + 3*i] == 'x') or \
           (board[0 + 3*i] == 'o' and board[1 + 3*i] == 'o' and board[2 + 3*i] == 'o'):
            pygame.draw.line(screen, blue, (10, 100 + 200*i), (590, 100 + 200*i), 40)
            pygame.display.flip()
            return True, False
    # Check for a win along columns
    for j in range(0, 3):
        if (board[0 + j] == 'x' and board[3 + j] == 'x' and board[6 + j] == 'x') or \
           (board[0 + j] == 'o' and board[3 + j] == 'o' and board[6 + j] == 'o'):
            pygame.draw.line(screen, blue, (100 + j*200, 10), (100 + j*200, 590), 40)
            pygame.display.flip()
            return True, False
    # Check for a win on the diagonal from upper left
    if (board[0] == 'x' and board[4] == 'x' and board[8] == 'x') or \
        (board[0] == 'o' and board[4] == 'o' and board[8] == 'o'):
        pygame.draw.line(screen, blue, (10, 10), (590, 590), 40)
        pygame.display.flip()
        return True, False
    # Check for a win on the diagonal from lower left
    if (board[2] == 'x' and board[4] == 'x' and board[6] == 'x') or \
        (board[2] == 'o' and board[4] == 'o' and board[6] == 'o'):
        pygame.draw.line(screen, blue, (10, 590), (590, 10), 40)
        pygame.display.flip()
        return True, False
    
    # Check for a tie only after we check for a win (because a win might also happen on move 9)
    for i in range(9):
        if board[i] == ' ':
            return False, False    # We found an empty space so the game is not over

    # To arrive here there are no empty spaces; and it is not a win for somebody...
    #   so that makes it a cat game (a tie)
    pygame.draw.arc(screen, blue, (50, 50, 500, 500), 0.3, 6.0, 40)
    pygame.display.flip()
    return True, True



#################
##
## Program begins doing things here
##
#################

print(pygame.__path__)

print('''

Welcome to Tic Tac Toe! You are X and you go First using these keys:

  Q     W     E

  A     S     D

  Z     X     C

Good luck!
''')

# set our screen's width and height
square = 200
screenWidth, screenHeight = (square*3, square*3)

pygame.init()
pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((screenWidth, screenHeight))


white = (255, 255, 255)   # color of moves
black = (0, 0, 0)         # background
blue = (0, 0, 255)        # marks wins and ties
green = (0, 255, 0)       # color of the grid lines

screen.fill(black)
pygame.draw.line(screen, green, (square, 0), (square, 3*square), 5)
pygame.draw.line(screen, green, (2*square, 0), (2*square, 3*square), 5)
pygame.draw.line(screen, green, (0, square), (3*square, square), 5)
pygame.draw.line(screen, green, (0, 2*square), (3*square, 2*square), 5)

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# test board for checking draws
# board = [' ','x','o','o','o','x','x','o','x']

DrawBoard()

# since 'running' starts out True this while loop will keep running over and over again
running = True
while running:

    # Wait until the user presses a key
    key = pygame.key.get_pressed()

    # legalByX is a flag that assumes (by being False) that X tried to make an illegal move
    legalByX = False
    
    # draw if user presses one of the nine move keys: qweasdzxc
    if key[pygame.K_q] or key[pygame.K_w] or key[pygame.K_e] or \
       key[pygame.K_a] or key[pygame.K_s] or key[pygame.K_d] or \
       key[pygame.K_z] or key[pygame.K_x] or key[pygame.K_c]:
        if key[pygame.K_q] and board[0] == ' ': board[0] = 'x'; legalByX = True
        if key[pygame.K_w] and board[1] == ' ': board[1] = 'x'; legalByX = True
        if key[pygame.K_e] and board[2] == ' ': board[2] = 'x'; legalByX = True
        if key[pygame.K_a] and board[3] == ' ': board[3] = 'x'; legalByX = True
        if key[pygame.K_s] and board[4] == ' ': board[4] = 'x'; legalByX = True
        if key[pygame.K_d] and board[5] == ' ': board[5] = 'x'; legalByX = True
        if key[pygame.K_z] and board[6] == ' ': board[6] = 'x'; legalByX = True
        if key[pygame.K_x] and board[7] == ' ': board[7] = 'x'; legalByX = True
        if key[pygame.K_c] and board[8] == ' ': board[8] = 'x'; legalByX = True
        DrawBoard()
        time.sleep(2)    # gives a little pause so more like playing a person
        evaluation = GameOver()
        if evaluation[0]:
            if evaluation[1]: print('Cat game (a tie)')
            else: print('X wins!')
            time.sleep(3); exit()
            
        # If we arrive here then there are still possible moves so it is O's turn
        #   O will move (and so on) only if X made a legal move
        if legalByX:
            MyMove()
            DrawBoard()
            evaluation = GameOver()
            if evaluation[0]:
                if evaluation[1]: print('Cat game (a tie)')
                else: print('O wins!')
                time.sleep(5); exit()
        
    # quit if user presses the space bar
    elif key[pygame.K_SPACE]: exit()

    # quit if something else happens to create a QUIT event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
