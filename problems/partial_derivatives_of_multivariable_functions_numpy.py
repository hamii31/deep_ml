import numpy as np
from numpy.polynomial import polynomial as P

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	x = point[0]
	y = point[1]
	if func_name == 'poly2d':
		df_dx = 2 * x * y + y**2 
		df_dy = x**2 + 2 * x * y 
		return (df_dx, df_dy)
	elif func_name == 'exp_sum':
		df_dx = np.exp(x + y)
		df_dy = np.exp(x + y)
		return (df_dx, df_dy)
	elif func_name == 'product_sin':
		df_dx = np.sin(y)
		df_dy = x * np.cos(y)
		return (df_dx, df_dy)
	elif func_name == 'poly3d':
		z = point[2]
		df_dx = 2 * x * y
		df_dy = x**2 + z**2
		df_dz = 2 * y * z
		return (df_dx, df_dy, df_dz)
	elif func_name == 'squared_error':
		df_dx = 2 * (x - y)
		df_dy = -2 * (x - y)
		return (df_dx, df_dy)
	
			

result = compute_partial_derivatives('poly3d', (1.0, 2.0, 3.0))
print(f"{result[0]:.1f},{result[1]:.1f},{result[2]:.1f}")
