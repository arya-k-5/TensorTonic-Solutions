import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    array = np.array(A)

    a,b = array.shape
    T = np.empty(shape=(b,a))
    for (r, c), value in np.ndenumerate(array):
        T[c,r] = value
    return T 

    