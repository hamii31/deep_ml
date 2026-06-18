import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X)
	X_T = X.T
	X_TX_inv = np.linalg.inv(np.dot(X_T, X))
	theta = np.dot(X_TX_inv, np.dot(X_T, y))
	return theta
