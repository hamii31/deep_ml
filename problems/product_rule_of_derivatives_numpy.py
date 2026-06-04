import numpy as np
from numpy.polynomial import polynomial as P

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    # Differentiate f and g

    f_prime = P.polyder(f_coeffs)
    g_prime = P.polyder(g_coeffs)

    # Polynomial multiplication 
    f_prime_g_product = np.convolve(f_prime, g_coeffs)
    g_prime_f_product = np.convolve(f_coeffs, g_prime)

    # Calculate the coefficients
    deriv_coeffs = []

    # Error handling
    if all(v == 0 for v in f_prime_g_product):
        return g_prime_f_product[0]
    elif all(v == 0 for v in g_prime_f_product):
        return f_prime_g_product[0]
    else:
        n = len(f_prime_g_product)
        for i in range(n):
            deriv_coeffs.append(f_prime_g_product[i] + g_prime_f_product[i])

    return deriv_coeffs
