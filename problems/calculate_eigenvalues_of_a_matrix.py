def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	tr = a + d
	det = (a*d) - (b*c)

	eigenvectors = []
	for i in range(9):
		for j in range(9):
			if i * j == det and i + j == tr:
				eigenvectors.append(i)
	
	eigenvectors = sorted(eigenvectors, reverse=True)
	return eigenvectors
