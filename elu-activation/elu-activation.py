import math
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    ans = []
    for i in x:
        if i > 0:
            ans.append(i)
        else:
            ans.append(alpha*(math.exp(i)-1))

    return ans 