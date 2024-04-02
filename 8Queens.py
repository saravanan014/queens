def solveNQueens(board, col):
	if col == N:
		print_solution(board)
		return True
	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 1
			if solveNQueens(board, col + 1):
				return True
			board[i][col] = 0
	return False

def isSafe(board, row, col):
	for x in range(col):
		if board[row][x] == 1:
			return False
	for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[x][y] == 1:
			return False
	for x, y in zip(range(row, N, 1), range(col, -1, -1)):
		if board[x][y] == 1:
			return False
	return True

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if cell == 1 else "_" for cell in row]))

N=8
board = [[0 for x in range(N)] for y in range(N)]
solveNQueens(board, 0)


