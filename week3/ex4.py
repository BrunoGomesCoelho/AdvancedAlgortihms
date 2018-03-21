import sys


def create_possible_answer(collumn, row, matrix):
	new_matrix = [ [matrix[x][y] for y in range(8)] for x in range(8) ]
	for j in range(8):
		if j != collumn:
			new_matrix[row][j] = not VALID
		if j != row:
			new_matrix[j][collumn] = not VALID
		if j != 0 and collumn + j < 8:
			if row + j < 8:
				new_matrix[row+j][collumn+j] = not VALID
			if row - j >= 0:
				new_matrix[row-j][collumn+j] = not VALID
	return new_matrix


def count_moves(queens, answer):
	total = 0
	for k in range(8):
		if answer[k] != queens[k]:
			total += 1
	return total


def backtracking_solver(collumn, matrix, queens, answer):
	if collumn == 8: # We have a valid answer
		moves = count_moves(queens, answer)
		global min_moves
		if moves < min_moves:
			min_moves = moves
	else:
		for i in range(8):
			if matrix[i][collumn] == VALID:
				answer[collumn] = i + 1
				new_matrix = create_possible_answer(collumn, i, matrix)
				backtracking_solver(collumn+1, new_matrix, queens, answer)
				answer[collumn] = -1


line = sys.stdin.readline().rstrip()
count = 0

while line:
	count += 1
	solved = False
	matrix = [8*[False] for x in range(8)]
	VALID = False

	queens = [int(x) for x in line.split()]
	min_moves = 8
	answer = 8*[-1]
	
	backtracking_solver(0, matrix, queens, answer)

	print("Case %d: %d" % (count, min_moves))

	line = sys.stdin.readline().rstrip()






