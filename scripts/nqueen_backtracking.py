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

# Create a template empty board filled with zeroes
empty_board = np.zeros((N,N), dtype = int).flatten()

class NQ():
    ''' Class that contains N-Queen's game logic'''
    def __init__(self, new_board=None):
        if new_board is None:
            self.board = np.copy(empty_board)
        else:
            self.board = new_board
        # Transform from 1 dimensional to 2 dimensional board.
        self.board_2d = self.board.reshape((N,N))
        # print(self.board_2d)

    def __str__(self):
        ''' Prints the board to the console in 2D'''
        return str(self.board)
    
    def fill(self, y):
        ''' Fill the board with a queen on each column'''
        if y >= N:
            return True
        for x in range(N):
            if self.check_conflicts(x, y):
                self.board_2d[x][y] = 1
                # Fill until a conflict is thrown
                if self.fill(y + 1) == True:
                    return True
                # Backtracking Step
                self.board_2d[x][y] = 0
        self.update(self.board_2d.flatten())
        return False

    def check_conflicts(self, x, y):
        ''' Returns True if there any no conflicts.'''
        if (self.check_cols(x,y)):
            return False
        if (self.check_diags(x,y)):
            return False
        return True

    def check_cols(self, x, y):
        ''' Checks if there are any queens in the column'''
        for i in range(y):
            if self.board_2d[x][i] == 1:
                return True
        return False
    
    def check_diags(self, x, y):
        ''' Checks if there are any queens in its diagonal'''
        i, j = x, y
        # Down Left
        while i >= 0 and j >= 0:
            if self.board_2d[i][j] == 1:
                return True
            i -= 1
            j -= 1

        i, j = x, y
        # Up Left
        while i < N and j >= 0:
            if self.board_2d[i][j] == 1:
                return True
            i += 1
            j -= 1
        return False
    
    def update(self, board):
        return NQ(board)

# Formulate the board
test_board = NQ()
test_board.fill(0)

print("BOARD:")
print(test_board.board.reshape(N,N))