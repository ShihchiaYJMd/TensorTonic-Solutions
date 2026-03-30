import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x_arr = np.asarray(x)
    p_arr = np.asarray(p)

    if x_arr.shape != p_arr.shape:
        raise ValueError

    prob_sum = np.sum(p_arr)
    if not np.isclose(prob_sum, 1.0, atol=1e-6):
        raise ValueError

    return np.sum(x_arr * p_arr)