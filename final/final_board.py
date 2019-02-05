# Name: David Adams
# CMS cluster login name: dmadams

'''
final_board.py

This module contains classes that implement the Connect-4 board object.
'''

from copy import *


class MoveError(Exception):
    '''
    Instances of this class are exceptions which are raised when
    an invalid move is made.
    '''
    pass

class BoardError(Exception):
    '''
    Instances of this class are exceptions which are raised when
    some erroneous condition relating to a Connect-Four board occurs.
    '''
    pass

class Connect4Board:
    '''
    Instance of this class manage a Connect-Four board, but do not
    manage the play of the game itself.
    '''

    def __init__(self):
        '''
        Initialize the board.
        '''
        board = []
        for i in range(7):
            board.append([])
            for j in range(6):
                board[i].append(0)
        self.board = board


    def getRows(self):
        '''
        Return the number of rows.
        '''
        return len(self.board[0])


    def getCols(self):
        '''
        Return the number of columns.
        '''
        return len(self.board)


    def get(self, row, col):
        '''
        Arguments:
          row -- a valid row index
          col -- a valid column index

        Return value: the board value at (row, col).

        Raise a BoardError exception if the 'row' or 'col' value is invalid.
        '''
        if type(row) != int:
            raise BoardError('row must be of type int.')
        if type(col) != int:
            raise BoardError('col must be of type int.')
        if 0 > row or row > 5:
            raise BoardError('row must be in the range 0 to 5.')
        if 0 > col or col > 6:
            raise BoardError('col must be in the range 0 to 6.')
        
        return self.board[col][row]


    def clone(self):
        '''
        Return a clone of this board i.e. a new instance of this class
        such that changing the fields of the new instance will not
        affect the old instance.

        Return value: the new Connect4Board instance.
        '''
        board_copy = Connect4Board()
        board_copy.board = deepcopy(self.board)
        return board_copy


    def possibleMoves(self):
        '''
        Compute the list of possible moves (i.e. a list of column numbers 
        corresponding to the columns which are not completely filled up).

        Return value: the list of possible moves
        '''
        lst = []
        for i in range(7):
            if 0 in self.board[i]:
                lst.append(i)
        return lst
        

    def makeMove(self, col, player):
        '''
        Make a move on the specified column for the specified player.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: none

        Raise a MoveError exception if a move cannot be made because the column
        is filled up, or if the column index or player number is invalid.
        '''
        if type(col) != int:
            raise MoveError('col must be of type int.')
        if type(player) != int:
            raise MoveError('player must be of type int.')
        if 0 > col or col > 6:
            raise MoveError('col must be in the range 0 to 6.')
        if player != 1 and player != 2:
            raise MoveError('player must be either 1 or 2.')
        if col not in self.possibleMoves():
            raise MoveError('Column %d is already filled.' % col)
        
        for i in range(6):
            if self.board[col][i] == 0:
                self.board[col][i] = player
                break
            

    def unmakeMove(self, col):
        '''
        Unmake the last move made on the specified column.

        Arguments:
          col -- a valid column index

        Return value: none

        Raise a MoveError exception if there is no move to unmake, or if the
        column index is invalid.
        '''
        if type(col) != int:
            raise MoveError('col must be of type int.')
        if 0 > col or col > 6:
            raise MoveError('col must be in the range 0 to 6.')        
        if 1 not in self.board[col] and 2 not in self.board[col]:
            raise MoveError('There are no moves to undo in column %d.' %col)
        
        for i in range(6):
            if self.board[col][5 - i] == 1:
                self.board[col][5 - i] = 0
                break
            if self.board[col][5 - i] == 2:
                self.board[col][5 - i] = 0
                break


    def colWin(self, col):
        '''Check to see if the last move played in column 'col' resulted in a 
        win in a column. Does not check for any errors.
        '''
        row = 5
        for k in range(6):
            if self.board[col][k] == 0:
                row -= 1
        min_row = row - 3
        max_row = row + 3
        if min_row < 0:
            min_row = 0
        if max_row > 5:
            max_row = 5
        p1 = 0
        p2 = 0
        for i in range(min_row, max_row + 1):
            if self.board[col][i] == 0:
                p1 = 0
                p2 = 0
            elif self.board[col][i] == 1:
                p1 += 1
                p2 = 0
            else:
                p2 += 1
                p1 = 0
            if p1 == 4 or p2 == 4:
                return True
        return False


    def rowWin(self, col):
        '''Check to see if the last move played in column 'col' resulted in a 
        win in a row. Does not check for any errors.
        '''
        row = 5
        for k in range(6):
            if self.board[col][k] == 0:
                row -= 1
        min_col = col - 3
        max_col = col + 3
        if min_col < 0:
            min_col = 0
        if max_col > 6:
            max_col = 6
        p1 = 0
        p2 = 0
        for i in range(min_col, max_col + 1):
            if self.board[i][row] == 0:
                p1 = 0
                p2 = 0
            elif self.board[i][row] == 1:
                p1 += 1
                p2 = 0
            else:
                p2 += 1
                p1 = 0
            if p1 == 4 or p2 == 4:
                return True
        return False
        

    def upDiagonalWin(self, col):
        '''Check to see if the last move played in column 'col' resulted in a 
        win in an upwards diagonal. Does not check for any errors.
        '''
        row = 5
        for k in range(6):
            if self.board[col][k] == 0:
                row -= 1
        if row > col:
            xrow = row - col
            xcol = 0
        else:
            xrow = 0
            xcol = col - row
        p1 = 0
        p2 = 0
        while xrow < 6 and xcol < 7:
            if self.board[xcol][xrow] == 0:
                p1 = 0
                p2 = 0
            elif self.board[xcol][xrow] == 1:
                p1 += 1
                p2 = 0
            else:
                p2 += 1
                p1 = 0
            if p1 == 4 or p2 == 4:
                return True
            xrow += 1
            xcol += 1
        return False
            

    def downDiagonalWin(self, col):
        '''Check to see if the last move played in column 'col' resulted in a 
        win in an downwards diagonal. Does not check for any errors.
        '''
        row = 5
        for k in range(6):
            if self.board[col][k] == 0:
                row -= 1
        if row + col <= 5:
            xcol = 0
            xrow = row + col
        else:
            xrow = 5
            xcol = (row + col) - 5
        p1 = 0
        p2 = 0
        while xrow >= 0 and xcol < 7:
            if self.board[xcol][xrow] == 0:
                p1 = 0
                p2 = 0
            elif self.board[xcol][xrow] == 1:
                p1 += 1
                p2 = 0
            else:
                p2 += 1
                p1 = 0
            if p1 == 4 or p2 == 4:
                return True
            xrow -= 1
            xcol += 1
        return False
        
    def isWin(self, col):
        '''
        Check to see if the last move played in column 'col' resulted in a win
        (four or more discs of the same color in a row in any direction).

        Argument: 
          col    -- a valid column index

        Return value: True if there is a win, else False

        Raise a BoardError exception if the column is empty (i.e. no move has
        ever been made in the column), or if the column index is invalid.
        '''
        if type(col) != int:
            raise BoardError('col must be of type int.')
        if 0 > col or col > 6:
            raise BoardError('col must be in the range 0 to 6.')        
        if 1 not in self.board[col] and 2 not in self.board[col]:
            raise BoardError('No moves have been made in column %d.' %col)
        
        if self.colWin(col):
            return True
        elif self.rowWin(col):
            return True
        elif self.upDiagonalWin(col):
            return True
        elif self.downDiagonalWin(col):
            return True
        return False


    def isDraw(self):
        '''
        Check to see if the board is a draw because there are no more
        columns to play in.

        Precondition: This assumes that there is no win on the board.

        Return value: True if there is a draw, else False
        '''

        if len(self.possibleMoves()) == 0:
            return True
        return False


    def isWinningMove(self, col, player):
        '''
        Check to see if making the move 'col' by the player 'player'
        would result in a win.  The board state does not change.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: True if the move would result in a win, else False.

        Precondition: This assumes that the move can be made.
        '''
        board2 = self.clone()
        row = 6
        for k in range(6):
            if self.board[col][k] == 0:
                row -= 1
        board2.board[col][row] = player
        return board2.isWin(col)
        

    def isDrawingMove(self, col, player):
        '''
        Check to see if making the move 'col' by the player 'player'
        would result in a draw.  The board state does not change.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: True if the move would result in a draw, else False.

        Precondition: This assumes that the move can be made, and that the
        move has been checked to see that it does not result in a win.
        '''
        board_copy = self.clone()
        row = 6
        for k in range(6):
            if self.board[col][k] == 0:
                row -= 1
        board_copy.board[col][row] = player
        return board_copy.isDraw()

