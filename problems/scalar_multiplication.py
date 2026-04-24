def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	sm_matrix = []
	for row in matrix:
		sm_matrix.append([e * scalar for e in row])

	return sm_matrix
