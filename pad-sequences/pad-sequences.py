import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs)

    # empty case
    if N == 0:
        return np.empty((0, 0), dtype=int)

    # determine L        
    L = max_len if max_len else max(len(seq) for seq in seqs)

    # dtpe = int
    pad_seqs = np.full((N, L), pad_value, dtype=int)

    # fill values
    for i, seq in enumerate(seqs):
        length = min(len(seq), L)
        if length > 0:
            pad_seqs[i, :length] = seq[:length]

    return pad_seqs
                