# Name: David Adams
# CMS cluster login name: dmadams

'''
final_players.py

This module contains code for various bots that play Connect4 at varying 
degrees of sophistication.
'''

import random
from Connect4Simulator import *


class RandomPlayer:
    '''
    This player makes one of the possible moves on the game board,
    chosen at random.
    '''

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        assert player in [1, 2]
        possibles = board.possibleMoves()
        assert possibles != []
        return random.choice(possibles)


class SimplePlayer:
    '''
    This player will always play a move that gives it a win if there is one.
    Otherwise, it picks a random legal move.
    '''

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        assert player in [1, 2]
        p = board.possibleMoves()
        for col in p:
            if board.isWinningMove(col, player):
                return col
        return random.choice(p)


class BetterPlayer:
    '''
    This player will always play a move that gives it a win if there is one.
    Otherwise, it tries all moves, collects all the moves which don't allow
    the other player to win immediately, and picks one of those at random.
    If there is no such move, it picks a random move.
    '''

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        assert player in [1, 2]
        p = board.possibleMoves()
        if len(p) == 1:
            return p[0]
        win = []
        bad = []
        good = []
        board2 = board.clone()
        for col in p:
            if board.isWinningMove(col, player):
                win.append(col)
            board2.makeMove(col, player)
            for col2 in board2.possibleMoves():
                if board2.isWinningMove(col2, 3 - player):
                    bad.append(col)
            board2.unmakeMove(col)
        for c in p:
            if c not in bad:
                good.append(c)
        if len(win) > 0:
            return random.choice(win)
        if len(good) > 0:
            return random.choice(good)
        return random.choice(p)


class Monty:
    '''
    This player will randomly simulate games for each possible move,
    picking the one that has the highest probability of success.
    '''

    def __init__(self, n, player):
        '''
        Initialize the player using a simpler computer player.

        Arguments: 
          n      -- number of games to simulate.
          player -- the computer player
        '''

        assert n > 0
        self.player = player
        self.n = n

    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        assert player in [1, 2]
        p = board.possibleMoves()
        move = p[0]
        wins = 0
        most_wins = 0
        for col in p:
            if board.isWinningMove(col, player):
                move = col
                break
            board.makeMove(col, player)
            for i in range(self.n):
                sim = Connect4Simulator(board.clone(), self.player, \
                                        self.player, 3 - player)                
                result = sim.simulate()
                if result == player:
                    wins += 1
            if wins > most_wins:
                most_wins = wins
                move = col
            board.unmakeMove(col)
            wins = 0
        return move
                

