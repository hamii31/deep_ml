import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	# ensure same dims
	if v1.shape != v2.shape:
		return
	
	# Calculate dot product and L2 norms
	n = len(v1)
	dot_product = 0
	vec1_l2 = 0
	vec2_l2 = 0
	for i in range(n):
		dot_product += v1[i] * v2[i]
		vec1_l2 += v1[i] ** 2
		vec2_l2 += v2[i] ** 2

	vec1_l2 = np.sqrt(vec1_l2)
	vec2_l2 = np.sqrt(vec2_l2)

	# Find cosine similarity
	cosine = dot_product / (vec1_l2 * vec2_l2)    
	return cosine
