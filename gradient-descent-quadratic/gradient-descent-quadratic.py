def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    
    count = 0
    x = x0
    #f'(x) = 2ax + b
    while count<steps:
        x = x - lr*( 2*a*x +b)
        count = count+1
    return x