import numpy as np
import copy

def machine_move(board, player):
    current_loc = getBestMove(board, player, 9)
    board[current_loc] = player
    return(board)

def getBestMove(board, player, depth):
    if board.any() == 0:
        return 0, 0

    me = player
    if me == 1:
        you = 2
    else:
        you = 1


    newBoard = copy.deepcopy(board)
    selection = possibilities(board)
    evals = [0 for i in selection]
    for i, move in enumerate(selection):
        newBoard[move] = me
        evals[i] = getBoardValue(newBoard, you, depth, depth)
        newBoard[move] = 0

    return selection[evals.index(max(evals))]

def getBoardValue(board, player, depth, maxDepth):

    me = player
    if me == 1:
        you = 2
    else:
        you = 1

    wl = -finalEval(board, me, you)
    if wl != 0 or depth <= 0:
        return wl*depth

    newBoard = copy.deepcopy(board)
    selection = possibilities(board)
    if selection == []:
        return finalEval(board, me, you)

    evals = [0 for i in selection]
    for i, move in enumerate(selection):
        newBoard[move] = me
        evals[i] = getBoardValue(newBoard, you, depth-1, maxDepth)
        newBoard[move] = 0
        if evals[i] > 0:
            break

    return -max(evals)

def finalEval(board, me, you):
    winner = evaluate(board)
    if winner == me:
        return 1
    elif winner == you:
        return -1
    else:
        return 0


def possibilities(board):
    ledig = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0 or board[i][j] == '0':
                ledig.append((i, j))
    return (ledig)  # ledig er en liste med ledig plasser, i.e (1,1), (2,3), osv)

def row_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue

        if win == True:
            return win
    return win

def col_win(board, player):
    for x in range(len(board)):
        win = True

        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue

        if win == True:
            return (win)
    return (win)

def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win

def evaluate(board):
    winner = 0

    for player in [1, 2]:
        if (row_win(board, player) or
                col_win(board, player) or
                diag_win(board, player)):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner