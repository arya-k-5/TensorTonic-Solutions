import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)
    
    if sum(p) != 1:
        raise ValueError
    if x.shape == p.shape:
        return (sum(x*p))