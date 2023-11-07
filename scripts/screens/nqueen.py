# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# N-Queens Board Logic
# ---
''' Problem Formulation:
    Variables: N_{i,j}, where N is the number of rows/columns
     used to form the checkered chess board, i is the piece's
     coordinate on the x-axis, and j is the piece's coordinate
     on the y-axis.
    Domain: {0,1}, either there exists a queen chess piece
     (denoted by 1) on the coordinates or not. (denoted by 0)
     '''

# Where N is the number of queens placed on each row.
N = 4

# Libraries
import numpy as np
import pandas as pd
import collections

# Create a template empty board filled with zeroes
empty_board = np.zeros((N,N), dtype = int).flatten()
# Formulate the board
class NQ():
    ''' Class that contains N-Queen's game logic'''
    def __init__(self, new_board=None, new_conflicts=None):
        if new_board is None:
            self.board = np.copy(empty_board)
            self.conflicts = np.copy(empty_board)
        else:
            self.board = new_board
            self.conflicts = new_conflicts
        # Transform from 1 dimensional to 2 dimensional board.
        self.board_2d = self.board.reshape((N,N))
        print(self.board_2d)

    def __str__(self):
        ''' Prints the board to the console in 2D'''
        return str(self.board)
    
    def random_fill(self):
        ''' Fill the board randomly with a queen on each row'''
        for i in range(N):
            j = np.random.choice(range(N), 1)[0]
            self.board_2d[i][j] = 1
        return NQ(self.board_2d.flatten())

    def test_conflicts(self):
        ''' Check if there exists a winning condition for symbol \'sym\' '''
        # Rotate to get columns.
        self.check_rows(self.board_2d)
        temp_board = np.rot90(np.copy(self.board_2d))
        print('ROT')
        print(temp_board)
        print('ROT')
        self.check_rows(temp_board)
        # self.check_diags(self.board_2d)
        # self.reduce_dupes()
        
    def check_rows(self, board):
        ''' Check rows for a winning combination'''
        for i,row in enumerate(board):
            for j,val in enumerate(row):
                if val == 1:
                    self.conflicts[N*i+j] += 1
        return NQ(self.board, self.conflicts)
    
    def check_diags(self, board):
        ''' Check diagonals for a winning combination'''
        self.conflicts_2d = self.conflicts.reshape((N,N))
        cd = np.diag_indices_from(board)
        for i,val in enumerate(board[cd]):
            if val == 1:
                self.conflicts_2d[cd][i] += 1
                print(self.conflicts_2d[cd][i])
        self.conflicts = self.conflicts_2d.flatten()
        return NQ(self.board, self.conflicts)
    
    def reduce_dupes(self):
        ''' This decreases the number of conflicts by the duplicate
            queens that had already been accounted for.'''
        for i in range(len(self.conflicts)):
            # Reduced by 1 for each direction searched (rows,cols,diag)
            self.conflicts[i] -= 3
        return NQ(self.board, self.conflicts)
    
test_board = NQ()
test_board.random_fill()
test_board.test_conflicts()
print("BOARD:")
print(test_board.board.reshape(N,N))
print("CONFLICTS:")
print(test_board.conflicts.reshape((N,N)))