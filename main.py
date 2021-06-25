import pygame, sys, random, copy, analysis
from pygame import *
import numpy as np

class boardRect():
    def __init__(self, x, y):
        self.index = x, y
        self.rect = pygame.Rect(x*100, y*100, 100, 100)

pygame.init()

WINDOWWIDTH, WINDOWHEIGHT = 300, 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Tic Tac Toe Analysis engine')

giantFont = pygame.font.SysFont('arialblack', 90)
normalFont = pygame.font.SysFont('arialblack', 15)

board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
boardRects = [boardRect(i, j) for j in range(3) for i in range(3)]

lines = []
lines.append(pygame.Rect(100, 0, 1, 300))
lines.append(pygame.Rect(200, 0, 1, 300))
lines.append(pygame.Rect(0, 100, 300, 1))
lines.append(pygame.Rect(0, 200, 300, 1))

currentPlace = 1

XOs = {1:'X', 2:'O', 0:''}


def displayFont(x, y, text, font, windowSurface, center=True, opacity=255):
    desc = font.render(text, True, BLACK, WHITE)
    desc.set_alpha(opacity)
    textRect = desc.get_rect()
    if center:
        textRect.center = x, y
    else:
        textRect.topleft = x, y
    windowSurface.blit(desc, textRect)

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

done = False

outcome = 'Up in the air'

resetText = normalFont.render('Reset', True, BLACK)
resetRect = resetText.get_rect()
resetRect.topleft = 250, 300

evaluation = 0  # Hard coded
bestMove = (0, 0)  # Hard coded

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            Mrect = pygame.Rect(x, y, 1, 1)
            if not done:
                for rect in boardRects:
                    if rect.rect.colliderect(Mrect):
                        if board[rect.index] == 0:
                            board[rect.index] = currentPlace
                            if currentPlace == 1:
                                currentPlace = 2
                            else:
                                currentPlace = 1

                done = evaluate(board)
                if done == -1:
                    outcome = 'Draw'
                elif done == 1:
                    outcome = 'X won'
                elif done == 2:
                    outcome = 'O won'
                done = (done == 1 or done == 2 or done == -1)

                if not done:

                    evaluation = analysis.getBoardValue(board, currentPlace, 9, 9)
                    bestMove = analysis.getBestMove(board, currentPlace, 9)

            if Mrect.colliderect(resetRect):
                board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
                outcome = 'Up in the air'
                done = False
                currentPlace = 1
                evaluation = 0 #Hard coded
                bestMove = (0, 0) #Hard coded


    windowSurface.fill(WHITE)

    for x, row in enumerate(board):
        for y, tile in enumerate(row):
            t = XOs[tile]
            displayFont(50+100*x, 50+100*y, t, giantFont, windowSurface)

    for line in lines:
        pygame.draw.rect(windowSurface, BLACK, line)

    windowSurface.blit(resetText, resetRect)

    displayFont(0, 300, 'Turn: '+XOs[currentPlace], normalFont, windowSurface, center=False)
    if done:
        displayFont(0, 325, 'Outcome: '+outcome, normalFont, windowSurface, center = False)

    else:
        displayFont(0, 325, 'Analysis:', normalFont, windowSurface, center=False)
        if evaluation < 0:
            displayFont(0, 350, 'Evaluation: ' +XOs[currentPlace]+ ' is winning!', normalFont, windowSurface, center=False)
        elif evaluation > 0:
            c = 1
            if currentPlace == 1:
                c = 2
            displayFont(0, 350, 'Evaluation: '+XOs[c]+' is winning!', normalFont, windowSurface, center=False)
        else:
            displayFont(0, 350, 'Evaluation: Tie', normalFont, windowSurface, center=False)

        displayFont(0, 375, 'Best move: '+str((bestMove[0]+1, bestMove[1]+1)), normalFont, windowSurface, center=False)


        displayFont(50+100*bestMove[0], 50+100*bestMove[1], XOs[currentPlace], giantFont, windowSurface, opacity=50)

    pygame.display.update()

