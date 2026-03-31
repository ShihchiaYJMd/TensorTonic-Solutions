import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y_arr = np.asarray(y)

    if len(y) == 0:
        return 0.0

    _, counts = np.unique(y, return_counts=True)

    probs = counts / len(y)
    valid_probs = probs[probs > 0]

    entropy = - np.sum(valid_probs * np.log2(valid_probs))
    return entropy
    

    