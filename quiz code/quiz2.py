"""
compute the maximal relative error of solving linear systems
given A, b, x_star
"""

import numpy as np
import scipy.linalg

A = np.array([[1.0, 0.0, 2.0],
              [1.0, 0.0, 1.9],
              [1.0, 3.0, 11.0]])

b = np.array([1.0, 
              1.0, 
              4.0])

x_star = np.array([0.999961, 
                   1.000019, 
                   0.000022])

# compute the residual vector # r = 
r = np.matmul(A,x_star)-b

# compute norm of r and b
r_norm = np.linalg.norm(r, 2)
b_norm = np.linalg.norm(b, 2)

# compute max relative error
max_rel_error = np.linalg.cond(A, 2) * (r_norm / b_norm)

print(round(max_rel_error, 5))
# 0.05479673455486552