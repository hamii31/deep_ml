import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
  # get squared gradients
	sq_gradient = []
	sq_gradient = [i ** 2 for i in gradient]
	# magnitude is the sqrt of the sum of the gradients to the power of two
	magnitude = np.sqrt(sum(sq_gradient))
	
  # the direction is a unit vector of the gradients divided by the magnitude
	# handle edge case
	if magnitude == 0:
		direction = [0 for i in gradient]
		desc_direction = [-i for i in direction]
		return {"magnitude":magnitude, "direction":direction, "descent_direction":desc_direction}
	
	direction = [i / magnitude for i in gradient]
	desc_direction = [-i for i in direction]
	return {"magnitude":magnitude, "direction":direction, "descent_direction":desc_direction}

result = gradient_direction_magnitude([-2.0, 3.0, -6.0]) 
print(f"{result['magnitude']:.4f},{[round(d,4) for d in result['descent_direction']]}")
