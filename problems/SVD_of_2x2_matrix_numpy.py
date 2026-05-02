import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    # Form transpose of A
    def transpose_2x2(M, MT):
        for row in range(2):
            for col in range(2):
                # i,j -> j, i
                MT[col][row] = M[row][col]

        return MT
    
    AT = np.zeros(A.shape)
    AT = transpose_2x2(A, AT)
    # print(AT)

    # Find ATA
    AT_A = AT @ A
    # print(AT_A)

    def eigenvalues_2x2(matrix):
        a, b = matrix[0][0], matrix[0][1]
        c, d = matrix[1][0], matrix[1][1]

        tr = a + d
        det = a*d - b*c

        # calculate eigenvalues through characteristic polynomial λ² − tr·λ + det = 0 -> λ = (tr ± √(tr² − 4·det)) / 2
        discriminant = tr**2 - 4*det
        lambda1 = (tr + np.sqrt(discriminant)) / 2
        lambda2 = (tr - np.sqrt(discriminant)) / 2

        eigenvalues = sorted([lambda1, lambda2], reverse=True)
        return eigenvalues
    
    # Find S 
    S = np.sqrt(np.array(eigenvalues_2x2(AT_A)))
    # print(S)

    # Find V
    lambdas = eigenvalues_2x2(AT_A)

    def eigenvector_2x2(M, lam):
        # Solve (M - lam*I) v = 0
        # Row [a-lam, b] · v = 0  →  v = [-b, a-lam] (or [b, lam-a])
        a, b = M[0][0] - lam, M[0][1]
        v = np.array([-b, a]) if abs(b) > 1e-10 or abs(a) > 1e-10 else np.array([1.0, 0.0])
        return v / np.linalg.norm(v)  # normalize to unit length

    v1 = eigenvector_2x2(AT_A, lambdas[0])
    v2 = eigenvector_2x2(AT_A, lambdas[1])
    V = np.column_stack([v1, v2])
    # print(V)

    # Find VT
    VT = np.zeros(V.shape)
    VT = transpose_2x2(V, VT)
    # print(VT)

    # find U
    U = (A @ V) / S   # broadcasts: each column of A@V divided by its σ

    # Check if calculations are correct
    # A_L = U @ np.diag(S) @ VT
    # print(A_L)
    
    return U, S, VT

U, S, Vt = svd_2x2_singular_values(np.array([[2, 1], [1, 2]]))
print(f'U: {np.round(U, 4).tolist()}')
print(f'S: {np.round(S, 4).tolist()}')
print(f'Vt: {np.round(Vt, 4).tolist()}')
