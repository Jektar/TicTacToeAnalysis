# TicTacToe Analysis Engine
A analysis engine I made for tic-tac-toe, using pygame in python

main.py is a simple pygame GUI that breaks down the analysis.
analyse.py can be used by other programs, as it breaks down a position in tic-tac-toe in multiple ways, as can be found in the functions.

This analysis uses a recusive search algorithm to figure out the best possible move and all possibilities, assuming perfect play from both players.
Due some (very) light implementations of alpha-betha prooing, the code, even though it is in python, is able to search through all possibilities in resonable time. 

Note: If the engine considers a position lost, it will not nessecarily reccomend moves that prolong the game for as long as possible, 
occasionally leading to some quite strange sugestiones.
