import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    arr = np.array(x)
    return (abs(arr)+arr)/2
            