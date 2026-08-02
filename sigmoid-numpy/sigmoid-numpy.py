import numpy as np
import math


def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    den = 1+(1/np.exp(x))


    return 1/den