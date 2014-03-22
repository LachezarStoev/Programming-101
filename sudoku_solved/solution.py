def column(matrix, i):
    return [row[i] for row in matrix]
def row(matrix,i):
	return matrix[i]
def take_submatrix_3x3(matrix,p,q):
	return [matrix[i][j] for i in range(p,p+3) for j in range(q,q+3)]
def is_array_solved(arr):
	unique_numbers=set(arr)
	restricted_numbers=[x for x in unique_numbers if x in range(1,10)]
	return len(arr) == len(restricted_numbers)
def sudoku_solved(sudoku):
	for i in range(0,len(sudoku)):
		if not is_array_solved(row(sudoku,i)) or not is_array_solved(column(sudoku,i)):
			return False
	all_submatrix_3x3=[is_array_solved(take_submatrix_3x3(sudoku,i,j)) for i in [0,3,6] for j in [0,3,6]]
	return sum(all_submatrix_3x3) != 0
