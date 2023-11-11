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

def diag_test(board, conflicts, x, y, type):
    num1 = 0
    num2 = 0
    conflict_count = 0
    match type:
            case 'UR':
                num1 = 1
                num2 = 1
            case 'DL':
                num1 = -1
                num2 = -1
            case 'DR':
                num1 = 1
                num2 = -1
            case 'UL':
                num1 = -1
                num2 = 1
    xn = x
    yn = y
    if board[xn][yn] == 1:
        while ((x >= 0) and (x < N)) and\
              ((y >= 0) and (y < N)):
            if board[x][y] == 1:
                conflict_count += 1
            x += num1
            y += num2
        conflicts[xn][yn] += conflict_count
    return conflicts

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
        # print(self.board_2d)

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
        # self.check_rows(self.board_2d)
        # self.correct = np.array([0,1,0,0,
        #                         0,0,0,1,
        #                         1,0,0,0,
        #                         0,0,1,0])
        # self.correct_2d = self.correct.reshape((N,N))

        self.check_cols(self.board_2d)
        self.check_diags(self.board_2d)
    
    def check_cols(self, board):
        ''' Check cols for a winning combination'''
        for j in range(N): # Column loop
            conflict_count = 0
            for i in range(N): # Row loop
                if board[i][j] == 1:
                    conflict_count += 1
            for i in range(N):
                if board[i][j] == 1:
                    self.conflicts[N * i + j] += conflict_count*4
        return NQ(self.board, self.conflicts)

    def check_diags(self, board):
        ''' Check diagonals for a winning combination'''
        self.conflicts_2d = self.conflicts.reshape((N,N))
        for i in range(N):
            for j in range(N):
                # UP-RIGHT Diagonal Check
                self.conflicts_2d = diag_test(board, self.conflicts_2d, x=i, y=j, type='UR')
                # DOWN-LEFT Diagonal Check
                self.conflicts_2d = diag_test(board, self.conflicts_2d, x=i, y=j, type='DL')                
                # DOWN-RIGHT
                self.conflicts_2d = diag_test(board, self.conflicts_2d, x=i, y=j, type='DR')
                # UP-LEFT Diagonal Check
                self.conflicts_2d = diag_test(board, self.conflicts_2d, x=i, y=j, type='UL')
        self.conflicts = self.conflicts_2d.flatten()
        return NQ(self.board, self.conflicts)
    
    def solve_board(self, max_constraint=-1, mc_idx=-1, mc_idy=-1, depth=0):
        self.conflicts_2d = self.conflicts.reshape((N, N))
        for idx, row in enumerate(self.board_2d):
            for idy, val in enumerate(row):
                if self.conflicts_2d[idx][idy] > max_constraint:
                    max_constraint = self.conflicts_2d[idx][idy]
                    mc_idx, mc_idy = idx, idy
        if max_constraint == 0:
            return NQ(self.board_2d.flatten(), self.conflicts_2d.flatten())
        
        self.board_2d[mc_idx][mc_idy] = 0
        if (mc_idx < N-1):
            mc_idx += 1
        self.board_2d[mc_idx][mc_idy] = 1
        self.test_conflicts()

        if depth < N:
            return self.solve_board(max_constraint, mc_idx, mc_idy + 1, depth + 1)
        self.conflicts = self.conflicts_2d.flatten()
        self.board = self.board_2d.flatten()
        return NQ(self.board_2d.flatten(), self.conflicts_2d.flatten())

    def solve(self):
        self.test_conflicts()
        self.solve_board()
        return

# Formulate the board
test_board = NQ()
test_board.random_fill()
test_board.test_conflicts()
# test_board.solve()
print("BOARD:")
print(test_board.board.reshape(N,N))
print("CONFLICTS:")
print(test_board.conflicts.reshape((N,N)))