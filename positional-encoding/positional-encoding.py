import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(seq_len)[:, None]    # (seq_len, 1)
    i = np.arange(d_model)[None, :]     # (1, d_model)

    angle = pos / pow(base, 2 * (i // 2) / d_model)    # (seq_len, d_model)

    PE = np.zeros((seq_len, d_model))
    PE[:, 0::2] = np.sin(angle[:, 0::2])
    PE[:, 1::2] = np.cos(angle[:, 1::2])

    return PE
    
    