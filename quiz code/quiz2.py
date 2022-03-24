import numpy as np
import scipy.linalg

A = np.array([[-1.0, 16.0, 0.0],
            [0.0, 4.0, 10.0],
            [1.0, -4.0, 40.0]])

b = np.array([17.0, 14.0, 35.0])

x_star = np.array([-0.99900385, 0.99991435, 1.0000192])

# compute the residual vector
r = np.matmul(A,x_star)-b

# compute norm of r 
r_norm = np.linalg.norm(r, 2)
b_norm = np.linalg.norm(b, 2)

# compute max relative error
max_rel_error = np.linalg.cond(A, 2) * (r_norm / b_norm)

print(max_rel_error)
# 0.05479673455486552