import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    # nums = []
    # A = np.array(A)
    # result = np.zeros((A.shape[1], A.shape[0]))
    # for i in range(A.shape[0]):
    #     for j in range(A.shape[1]):
    #         nums.append(A[i][j])
    # for i in range(A.shape[1]):
    #     for j in range(A.shape[0]):
    #         result[i][j] = nums[j * A.shape[1] + i]
    
    # return result
    A = np.array(A)
    row, col = A.shape[0], A.shape[1]
    result = np.zeros((col, row))
    for i in range(row):
        for j in range(col):
            result[j][i] = A[i][j]

    return result