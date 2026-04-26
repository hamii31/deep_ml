import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	# Convert to numpy arrays
	a, b = np.array(a, dtype=float), np.array(b, dtype=float)
	
    # Check if a's column shape matches b's row shape
	if a.shape[1] != b.shape[0]:
		return -1
	
    # Return the product of the multiplied matricx
	return a @ b
