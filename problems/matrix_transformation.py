import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	# Convert to numpy arrays
    A, T, S = np.array(A, dtype=float), np.array(T, dtype=float), np.array(S, dtype=float)
    
    # Check if T and S are invertible
    if np.linalg.matrix_rank(T) < T.shape[0] or np.linalg.matrix_rank(S) < S.shape[0]:
        return -1

    # calculate the product of A, S and the inverse of T
    result = A @ S @ np.linalg.inv(T)

    return result.tolist()
