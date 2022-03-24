# CSCI / MATH 2072U -- Computational Science 1
# Tutorial 3
# PA=LU decomposition
#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007

import numpy as np
import scipy
import scipy.linalg
from copy import copy

# Note: indices i,j and k are used as matrix indices (starting from 1) while s is used as python array index (starting from 0)

def swap(M, i, j, m):
    # Swap rows i and j, only swap elements before m
    # NOTE: pass m = np.shape(M)[0] + 1 to swap all elements of that row
    # Indices in this function are used as Python array indeces (starting from 0)

    M[[i, j], :m] = M[[j, i], :m] 

    return M

def LUP(A):
    N = np.shape(A)[0]                         # extract matrix size
    
    U = copy(A)                                   # copy content of A (avoid linking U and A)
    L = np.identity(N)                         # initialize L and P
    P = np.identity(N)

    # loop through pivot columns
    for j in range(N):                        
        # find pivot element, max element on that column
        row_max = np.argmax(abs(U[j:N, j])) + j

         # if the pivot is not on the diagonal...
        if (row_max != j):                           
            # swap rows of U
            swap(U, row_max, j, N + 1)
            
            if j > 0:
                # swap rows of L left of diagonal element
                swap(L, row_max, j, j)

            # swap rows of P
            swap(P, row_max, j, N + 1)
            
        for i in range(j + 1, N):       # Gauss elimination of rows below pivot
            L[i, j] = U[i, j] / U[j, j]
            U[i, j:N] = U[i, j:N] - L[i, j] * U[j, j:N]
        

    return L, U, P

def results(A):
    L, U, P = LUP(A)

    print('Matrix is\n')
    print(A)
    print('\n')

    print('L=')
    print(L)
    print('\n')

    print('U=')
    print(U)
    print('\n')

    print('P=')
    print(P)
    print('\n')

    print('PA=')
    print(np.matmul(P, A))
    print('\n')

    print('LU=')
    print(np.matmul(L, U))
    print('\n')

    print('LU - PA=')
    print(np.matmul(P, A) - np.matmul(L, U))
    print('\n')

# A = np.array([[2., 2., 1.], 
#               [2., 2., -1.], 
#               [1., -1., 0.]])
A = np.array([[2.4, -3.3, -1.0], 
              [1.5, -1.2, 0.3], 
              [2.2, 2.9, 1.3]])

# A2 = np.array([[2.,1.,1.,0.],
#               [4.,3.,3.,1.],
#               [8.,5.,5.,1.],
#               [6.,7.,9.,8.]])


results(A)
L, U, P = LUP(A)
print("----------------------------------------")
# results(A2)
# print(np.argmax(abs(A), 0))



print(np.dot(P, np.array([1., 2., 3.])))