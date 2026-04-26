import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	# initialize x with zeros
    x = np.zeros(b.shape)

    # get diagonal and construct a matrix out of the off-diagonal elements
    a_ii = np.diagonal(A)
    a_ij = A - np.diag(a_ii)

    # instead of iterating over every equation we solve the entire system of equations until convergence
    for _ in range(n):
       x = (b - a_ij @ x) / a_ii

    x = [round(i,4) for i in x.tolist()]

    return x
