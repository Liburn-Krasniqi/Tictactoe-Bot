"""
Tic Tac Toe Player
"""

import copy
import math

# class IllegalActionError(Exception):
#     def __init__(self, value):
#         self.value = value
 
#     def __str__(self):
#         return(repr(self.value))

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = count_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == O:
                count_o += 1

    return (X, O)[count_x > count_o]


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if (terminal(board)):    
        return utility(board)

    actions = set()
    i = j = 0
    for row in board:
        j = 0
        for cell in row:
            if cell == EMPTY:
                actions.add((i, j))  
            j += 1
        i += 1       
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    legalActions = actions(board)  # not as in lawsuits
    if action not in legalActions:
        raise Exception("Illegal Action on board")
    
    turn = player(board)
    
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = turn

    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (utility(board) == -1):
        return O
    if (utility(board) == 1):
        return X
    else:
        return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_cell = False
    count_x = count_o = count_xd = count_od = count_xdi = count_odi = count_xdig = count_odig = 0      
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1  
            elif board[i][j] == O:
                count_o += 1
            else:
                empty_cell = True

            if board[j][i] == X:
                count_xd += 1  
            elif board[j][i] == O:
                count_od += 1
        if (count_o == 3 or count_x == 3 or count_od == 3 or count_xd == 3):
            return True
        count_o = count_x = 0
        count_od = count_xd = 0

        if board[2-i][i] == X:
            count_xdig += 1  
        elif board[2-i][i] == O:
            count_odig += 1
        if board[i][i] == X:
            count_xdi += 1  
        elif board[i][i] == O:
            count_odi += 1
        if (count_odi == 3 or count_xdi == 3 or count_odig == 3 or count_xdig == 3):
            return True
    if (empty_cell == False):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    count_x = count_o = count_xd = count_od = count_xdi = count_odi = count_xdig = count_odig = 0      
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1  
            elif board[i][j] == O:
                count_o += 1

            if board[j][i] == X:
                count_xd += 1  
            elif board[j][i] == O:
                count_od += 1
        if (count_o == 3 or count_od == 3):
            return -1
        elif (count_x == 3 or count_xd == 3):
            return 1
        count_o = count_x = 0
        count_od = count_xd = 0

        if board[2-i][i] == X:
            count_xdig += 1  
        elif board[2-i][i] == O:
            count_odig += 1
        if board[i][i] == X:
            count_xdi += 1  
        elif board[i][i] == O:
            count_odi += 1
        if (count_odi == 3 or count_odig == 3):
            return -1
        elif (count_xdi == 3 or count_xdig == 3):
            return 1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):  # check if game over
        return None
    if board == initial_state():
        return (1, 1)

    turn = player(board)  # set whose turn it is
    optimalAction = None
    legalActions = actions(board)
    if turn == X:  # check whose turn it is
        v = -math.inf  # kinda like dijkstras algo here
        for action in legalActions:
            # searches for best outcome for that specific action RECURSIVELY

            max = min_value(result(board, action)) 
            if (max > v):  # if that outcome better or same compared to current chosen action 
                v = max  # ...replace with new max value 
                optimalAction = action  # and new action
    elif turn == O:
        v = math.inf
        for action in legalActions:
            min = max_value(result(board, action))
            if (min < v):
                v = min
                optimalAction = action
    return optimalAction
    

def max_value(board):
    """
    minmax helper function
    """
    if terminal(board):  # check if game over 
        return utility(board)  # if yes return winner value
    v = -math.inf  
    legalActions = actions(board)
    for action in legalActions:
        # for each action check best outcome in the eyes of the opponent recursively

        v = max(v, min_value(result(board, action)))  
    return v


def min_value(board):
    """
    minmax helper function
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    legalActions = actions(board)
    for action in legalActions:
        v = min(v, max_value(result(board, action)))
    return v
