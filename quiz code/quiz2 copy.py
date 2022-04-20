"""
question 8
solving system of linear equations using LUP
"""
import numpy as np
import scipy.linalg

A = np.array([
    [1.3, 2.0, -1.3],
    [2.3, 0.1, -1.1],
    [0.2, 2.1, -0.2]
])

b = np.array(
    [0.4, 
    0.1, 
    1.2])

x = scipy.linalg.solve(A, b)
print(x[0])