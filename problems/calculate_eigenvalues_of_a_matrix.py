def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    # Find the trace of the 2x2 matrix
    tr = a + d

    # Find the determinant of the 2x2 matrix
    det = (a*d) - (b*c)

    # Find the eigenvalues
    eigenvalues = []
    for i in range(9):
        for j in range(9):
            if i * j == det and i + j == tr:
                eigenvalues.append(i)    
    eigenvalues = sorted(eigenvalues, reverse=True)
    return eigenvalues
    

print(calculate_eigenvalues([[2, 1], [1, 2]]))
