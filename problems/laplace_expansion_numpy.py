def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	n = len(matrix)
	if n == 2:
		return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	total = 0
	for j in range(n):
		# minor is the matrix without row 0 and column j
		minor = [[row[k] for k in range(n) if k != j] for row in matrix[1:]] 
		total += ((-1)**j) * matrix[0][j] * determinant_4x4(minor)

	return total
