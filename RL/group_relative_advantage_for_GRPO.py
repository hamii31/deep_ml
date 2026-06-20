import numpy as np

def compute_group_relative_advantage(rewards: list[float]) -> list[float]:
	"""
	Compute the Group Relative Advantage for GRPO.
	
	For each reward r_i in a group, compute:
	A_i = (r_i - mean(rewards)) / std(rewards)
	
	If all rewards are identical (std=0), return zeros.
	
	Args:
		rewards: List of rewards for a group of outputs from the same prompt
		
	Returns:
		List of normalized advantages
	"""
	# Your code here
	mean = np.mean(rewards)
	std = np.std(rewards)
  n = len(rewards)

	if std == 0.0:
		# Generate an array of zeros equal to the size of rewards
		return [0.0] * n
	
	return (
		[(rewards[i]-mean) / std for i in range(n)]
	)

rewards = [1.0, 1.0, 1.0, 1.0]
result = compute_group_relative_advantage(rewards)
print([round(v, 4) for v in result])
