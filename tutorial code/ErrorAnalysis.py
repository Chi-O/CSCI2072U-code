from sys import flags
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt

# helper function to build matrix of given size
def build_matrix(n):
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matrix[i, j] = ((-1) ** (i + j))/(i + 2 * j + 3)
        
    return matrix


# store matrix sizes
# for matrix sizes N = 2, ..., 10
matrix_sizes = range(2, 11)

# defining the three vectors we need
residual = np.ones(np.shape(matrix_sizes))
rel_error = np.ones(np.shape(matrix_sizes))
maximal_rel_error = np.ones(np.shape(matrix_sizes))

index = 0

# iterator = np.nditer(matrix_sizes, flags=['f_index'])
for size in matrix_sizes:
    # build matrix, A =
    matrix = build_matrix(size)
    # print("MATRIX SIZE", size)

    # we know exact solution x = e1; note this is a column vector (one column)
    exact_solution = np.zeros((size, 1))
    exact_solution[0] = 1.0

    # get computed solution using LUP decompostion, x =
    comp_solution = np.linalg.solve(matrix, matrix[:, [0]])

    # calculate residual vector, using l2 norm
    # || Ax - b || / || b || 
    residual[index] = np.linalg.norm(np.dot(matrix, comp_solution) - matrix[:, [0]], 2) / np.linalg.norm(matrix[:, [0]], 2)

    # calculate error vector, using l2 norm
    # || computed solution - exact solution || / || exact solution ||
    rel_error[index] = np.linalg.norm(comp_solution - exact_solution, 2) / np.linalg.norm(exact_solution, 2)

    # calculate maximal error vector, using l2 norm
    maximal_rel_error[index] = np.linalg.cond(matrix, 2) * residual[index]

    index += 1

# # print statements for result checking
# print("residual: ", residual) 
# print("relative error: ", rel_error) 
# print("maximal relative error: ", maximal_rel_error) 

plt.semilogy(matrix_sizes, rel_error, '-r', matrix_sizes, maximal_rel_error, '-c', matrix_sizes, residual, '-g')
plt.legend(['relative error', 'maximal error', 'residual'])
plt.xlabel('matrix size')
plt.ylabel('error')
plt.show()