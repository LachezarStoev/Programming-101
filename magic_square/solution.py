def column(matrix, i):
    return [row[i] for row in matrix]
def row(matrix,i):
	return matrix[i]
def magic_square(matrix):
	magic_number = sum(row(matrix, 0))
	for i in range(0,len(matrix)):
		if sum(row(matrix, i)) != magic_number or sum(column(matrix,i)) != magic_number:
			return False
	main_diagonal=sum([matrix[i][i] for i in range(0,len(matrix))])
	opposite_diaognal=sum([matrix[len(matrix)-i-1][i] for i in range(0,len(matrix))])
	return main_diagonal == magic_number and opposite_diaognal == magic_number