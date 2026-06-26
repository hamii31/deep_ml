import numpy as np
from collections import Counter

def pass_at_1(responses_correct: np.ndarray) -> float:
	"""
	Compute pass@1 by averaging correctness.
	
	Args:
		responses_correct: Boolean array for each response
		
	Returns:
		pass@1 score
	"""
	# Your code here
	occurences = Counter(responses_correct)
	return occurences[1] / len(responses_correct)


def majority_voting(responses: list[str]) -> str:
	"""
	Return the most common response.
	
	Args:
		responses: List of response strings
		
	Returns:
		Most frequent response
	"""
	# Your code here
	occurences = Counter(responses)
	return occurences.most_common(1)[0][0]


def pass_at_k(n: int, c: int, k: int) -> float:
	"""
	Compute unbiased pass@k from n samples with c correct.
	
	Formula: pass@k = 1 - C(n-c, k) / C(n, k)
	
	Args:
		n: Total samples
		c: Correct samples
		k: k in pass@k
		
	Returns:
		Estimated pass@k
	"""
	# Your code here
	return 1 - (n-c / k) / (n/k)
