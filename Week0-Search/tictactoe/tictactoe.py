"""
Tic Tac Toe Player
"""

import math
import copy

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
    #initialize X and O counts
    countX = 0
    countO = 0
    
    #count the number of X's O's on the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1
    
    #return the players turn
    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #initialize an empty set of all possible_actions
    all_possible_actions = set()
    
    #determine which cells are empty on the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                all_possible_actions.add((row, col))
    
    return all_possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise exception for invalid action
    if action not in actions(board):
        raise Exception("Invalid action")
    
    #define the cell for a given action
    row, col = action
    
    #make a deep copy of the original board
    board_copy = copy.deepcopy(board)
    
    #modify the board copy for the current players turn
    board_copy[row][col] = player(board)
    
    return board_copy


def check_rows(board, player):
    """
    Function to check for a winner along any rows
    """
    #check the board rows
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def check_cols(board, player):
    """
    Function to check for a winner along any cols
    """
    #check the board cols
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def check_diagonals(board, player):
    """
    Function to check for a winner along any diagonal
    """
    #check main diagonal
    if all(board[i][i] == player for i in range(len(board))):
        return True
    
    #check secondary diagonal
    if all(board[i][len(board) - 1 - i] == player for i in range(len(board))):
        return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #if any cells contain three X's in a row
    if check_rows(board, X) or check_cols(board, X) or check_diagonals(board, X):
        return X
    
    #if any cells contain three O's in a row
    elif check_rows(board, O) or check_cols(board, O) or check_diagonals(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #if X wins
    if winner(board) == X:
        return True
    #if O wins
    if winner(board) == O:
        return True
    #if tie
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    """
    Returns the highest value of transition model
    """
    #initialize a min value
    v = -math.inf
    
    #return the board utility at terminal state
    if terminal(board):
        return utility(board)
    
    #return the max value from the transition_model
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Returns the lowest value of transition model
    """
    #initialize a min value
    v = math.inf
    
    #return the board utility at terminal state
    if terminal(board):
        return utility(board)
    
    #return the max value from the transition_model
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #if the game is over
    if terminal(board):
        return None
    
    #case of player X (max-player)
    #---
    elif player(board) == X:
        plays = []
        #loop through possible actions
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        
        #reverse sort for the list of plays and return the action that should be taken
        return sorted(plays, key = lambda x: x[0], reverse = True)[0][1]
    
    #case of player O (min-player)
    #---
    elif player(board) == O:
        plays = []
        #loop through possible actions
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        
        #reverse sort for the list of plays and return the action that should be taken
        return sorted(plays, key = lambda x: x[0])[0][1]
