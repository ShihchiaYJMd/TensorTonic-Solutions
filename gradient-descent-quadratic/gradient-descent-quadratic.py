def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    """
    f(x) = ax^2 + bx + c
    f'(x) = 2ax + b
    x = x - lr * f'
    """
    for _ in range(steps):
        x0 -= lr * (2 * a * x0 + b)

    return x0
    