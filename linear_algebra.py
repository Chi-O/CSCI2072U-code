import numpy as np
import scipy

A = np.array([[-7, -5, 3], [-1, -8, 2], [1, 4, -1]])

print("the matrix A = ")
print(A)

# find the transpose 
B = A.T

# TODO: or using scipy 

# identity matrix
id_matrix = np.identity(4)

# zero matrix
zero_matrix = np.zeros((3, 3))

print(id_matrix)
print(zero_matrix)