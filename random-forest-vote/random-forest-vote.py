import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    preds = np.array(predictions)
    n_samples = preds.shape[1]

    result = []

    for i in range(n_samples):
        result.append(int(np.argmax(np.bincount(preds[:, i]))))

    return result