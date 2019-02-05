'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        board = []
        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(0)
        self.board = board
        self.move_lst = []

    def load(self, fname):
        '''Takes a filename fname as an argument. Loads fname, which must be of
        the proper format, and sets the board to the equivalent of fname.
        '''
        f = open(fname, 'r')
        c = 0
        for line in f:
            if len(line) != 10:
                raise IOError('%s is in an invalid format and cannot be ' \
                              'loaded.' %fname)
            try:
                for i in range(len(line) - 1):
                    if int(line[i]) > 9 or int(line[i]) < 0:
                        raise IOError('%s is in an invalid format and cannot ' \
                                      'be loaded.' %fname)
            except ValueError:
                raise IOError('%s is in an invalid format and cannot be ' \
                              'loaded.' %fname)
            c += 1
        if c != 9:
            raise IOError('%s is in an invalid format and cannot be loaded.' \
                          %fname)
        x = 0
        for line in f:
            y = 0
            for num in line:
                if y > 8:
                    break
                self.board[x][y] = int(num)
                y += 1
            x += 1
        f.close()

    def save(self, fname):
        '''Takes a filename fname as an argument. Saves the current state of the
        board to fname. 
        '''
        f = open(fname, 'w')
        for i in range(9):
            for j in range(9):
                f.write(str(self.board[i][j]))
            f.write('\n')
        f.close()

    def show(self):
        '''Pretty-print the current board representation.'''
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print

    def move(self, row, col, val):
        '''Takes three arguments row, col, and val, which must all be ints
        between 1 and 9. Enters val at the location (row, col) on the board if
        that is a valid move.
        '''
        if type(row) != int:
            raise SudokuMoveError('The row must be of type integer.')
        if type(col) != int:
            raise SudokuMoveError('The col must be of type integer.')
        if type(val) != int:
            raise SudokuMoveError('The val must be of type integer.')
        if row < 1 or row > 9:
            raise SudokuMoveError('The row must be an int in the range 1 to 9.')
        if col < 1 or col > 9:
            raise SudokuMoveError('The col must be an int in the range 1 to 9.')
        if val < 1 or val > 9:
            raise SudokuMoveError('The val must be an int in the range 1 to 9.')
        
        if self.board[row - 1][col - 1] != 0:
            raise SudokuMoveError('The location is not empty.')
        for x in self.board[row - 1]:
            if x == val:
                raise SudokuMoveError('There is already a %d in this row.' %val)
        for y in self.board[col - 1]:
            if y == val:
                raise SudokuMoveError('There is already a %d in this column.' \
                                      %val)
        for z in [self.board[row-2][col-2], self.board[row][col-2], \
                  self.board[row-2][col], self.board[row][col]]:
            if z == val:
                raise SudokuMoveError('There is a already a %d in this box.' \
                      %val)
        
        self.move_lst.append((row, col, val))
        self.board[row - 1][col - 1] = val

    def undo(self):
        '''Undoes the last move.
        '''
        if len(self.move_lst) == 0:
            raise SudokuCommandError('No moves have been made to undo.')
        last_move = self.move_lst.pop()
        self.board[last_move[0] - 1][last_move[1] - 1] = 0

    def solve(self):
        '''Begins an infinite loop in which the Sudoku game can be played.
        '''
        while True:
            cmnd = raw_input('Please enter a move:')
            try:
                if len(cmnd) == 0:
                    raise SudokuCommandError('Please enter a command.')
                elif cmnd == 'q':
                    return
                elif cmnd == 'u':
                    self.undo()
                    self.show()
                elif cmnd[0] == 's' and cmnd[1] == ' ' and len(cmnd) > 2:
                    self.save(cmnd[2:])
                elif len(cmnd) == 3 and 1 <= int(cmnd[0]) and 9 >= int(cmnd[0])\
                     and 1 <= int(cmnd[1]) and 9 >= int(cmnd[1]) \
                     and 1 <= int(cmnd[2]) and 9 >= int(cmnd[2]):
                    self.move(int(cmnd[0]), int(cmnd[1]), int(cmnd[2]))
                    self.show()
                else:
                    raise SudokuCommandError('%s is not a valid command.' %cmnd)
            except SudokuMoveError, e:
                print e
            except SudokuCommandError, e:
                print e
            except ValueError:
                print '%s is not a valid command.' %cmnd

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e

    s.show()
    s.solve()

