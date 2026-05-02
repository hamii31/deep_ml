import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	"""
	Normal Equation:
	    θ=(XTX)^−1 * XT * y
	Explanation of Terms

        ( X^T ) is the transpose of ( X ).
        ( (X^TX)^{-1} ) is the inverse of the matrix ( X^TX ).
        ( y ) is the vector of target values.

	"""
	# Your code here, make sure to round
	# Find T of X
	X = np.array(X)
	XT = X.T
	# print(XT)
	
    # Find XTX
	XT_X = XT @ X
	# print(XT_X)
	
    # Find the inverse of XTX
	XT_X_inv = np.linalg.inv(XT_X)
	# print(XT_X_inv)
	
    # Find theta
	theta = XT_X_inv @ XT @ y
	theta = np.round(theta,4)
	# print(theta)
	return theta
	

print(linear_regression_normal_equation([[1, 1], [1, 2], [1, 3]], [1, 2, 3]))
