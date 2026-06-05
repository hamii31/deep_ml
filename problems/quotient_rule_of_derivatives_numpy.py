import numpy as np
from numpy.polynomial import polynomial as P

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    # Calculate g(x)
    p_g_x = np.polyval(g_coeffs, x) # creates polynomial in desc order and evaluates at point x
    # Calculate g'(x)
    g_prime = P.polyder(g_coeffs[::-1]) # get derivative of desc order polynomial
    g_prime_x = P.polyval(x, g_prime)
    print(f"g(x)={p_g_x}")
    print(f"g'(x)={g_prime_x}")
    
    # Repeat for h
    p_h_x = np.polyval(h_coeffs, x)
    h_prime = P.polyder(h_coeffs[::-1])
    h_prime_x = P.polyval(x, h_prime)
    print(f"h(x)={p_h_x}")
    print(f"h'(x)={h_prime_x}")

    # Quotient rule
    f_prime_x = ((g_prime_x * p_h_x) - (p_g_x * h_prime_x)) / (p_h_x ** 2)
    return f_prime_x
    

print(round(quotient_rule_derivative([1, 0, 1], [1, 2], 2.0), 4))
