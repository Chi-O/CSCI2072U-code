# LU decomposition without pivoting (not for practical use)

import numpy as np

def LU(A):
    N = np.shape(A)[0]  # get row/col dimension of A 

    # initialize matrices
    U = np.copy(A)      # use np.copy() not assignment (to avoid using pointers and modifies the original array)
    L = np.identity(N)  # identity matrix of size A

    for j in range(N - 1):             # looping over columns (pivots); excluding the last row
        for i in range(j + 1, N):      # start from the entry below the pivot
            L[i, j] = U[i, j] / U[j, j]

            U[i, :] = U[i, :] - L[i, j] * U[j, :]

    return L, U

A = np.array([[2.2, 2.9, 1.3], 
              [2.4, -3.3, -1.0], 
              [1.5, -1.2, 0.3]])

L, U = LU(A)

print("L: \n", L)
print("\nU: \n", U)

print("is A = LU? \n")
print("LU: \n", np.dot(L, U))

print("\nA: \n", A)

print(A - np.dot(L, U))