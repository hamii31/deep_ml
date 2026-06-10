import numpy as np

# Helper functions
def sin(x, rule=None):
    """
    f(x) = sin(x)
    f'(x) = cos(x)
    """
    if rule == 'deriv':
        return np.cos(x)
    return np.sin(x)

def square(x, rule=None):
    """
    f(x) = x**2
    f'(x) = 2x
    """
    if rule == 'deriv':
        return 2*x
    return x**2
    
def exp(x):
    """
    f(x) = exp(x)
    f'(x) = exp(x)
    """
    return np.exp(x)

def log(x, rule=None):
    """
    f(x) = ln(x)
    f'(x) = 1/x
    """
    if rule == 'deriv':
        return 1/x
    return np.log(x)

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    deriv = 1.0 # accumulated product of the derivatives

    # right to left (get innermost first, work your way up to the outside)
    for name in reversed(functions):
        if name == 'sin':
            deriv = sin(x, rule='deriv') * deriv
            x = sin(x)
        elif name == 'square':
            deriv = square(x, rule='deriv') * deriv
            x = square(x)
        elif name == 'exp':
            deriv = exp(x) * deriv
            x = exp(x)
        elif name == 'log':
            deriv = log(x, rule='deriv') * deriv
            x = log(x)
    
    return deriv
		

result = compute_chain_rule_gradient(['sin', 'square'], 1.0); print(f"{result:.6f}")
result = compute_chain_rule_gradient(['exp', 'sin', 'square'], 0.5); print(f"{result:.6f}")
result = compute_chain_rule_gradient(['log', 'exp'], 2.0); print(f"{result:.6f}")
result = compute_chain_rule_gradient(['sin'], 0.785398); print(f"{result:.6f}")
result = compute_chain_rule_gradient(['exp', 'square'], 1.0); print(f"{result:.6f}")
