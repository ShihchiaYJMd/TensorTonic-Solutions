import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x, dtype=np.float32)

    # generate random matrix
    if not rng:
        rng = np.random
    r = rng.random(x.shape)

    mask = r > p
    
    output = x * mask / (1 - p)
    dropout_pattern = mask / (1 - p)

    return output, dropout_pattern
        
    