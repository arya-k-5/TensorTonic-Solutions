import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    na = np.sqrt(np.sum(a**2))
    nb = np.sqrt(np.sum(b**2))
    if na != 0 and nb!=0:
        return np.dot(a,b)/(na*nb)
    else:
        return 0 