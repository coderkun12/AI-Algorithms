import numpy as np

def isSafe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solveNQUtil(board, col, N):
    if col >= N:
        return board, True
    for i in range(N):
        if isSafe(board, i, col, N):
            board[i][col] = 1
            board, j = solveNQUtil(board, col + 1, N)
            if j == True:
                return board, True
            board[i][col] = 0
    return board, False

dimn = int(input("Enter the dimension of the square: "))
if dimn == 3:
    print("It is impossible to place three queens in a 3*3 area! Please try again with a number greater than 3.")
else:
    array = np.zeros([dimn, dimn])
    array, m = solveNQUtil(array, 0, dimn)
    if m == True:
        print(array)
    else:
        print("Solution not found.")
