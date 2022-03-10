"""
Function NewtonSystem Input:
Initializations:
For k = 
    Evaluate the residual vector:
    Evaluate the Jacobian: 
    Solve the linear system: 
    Update the solution    
Check for convergence: 
end for 

2072U, Winter 2022
"""

import numpy as np
import scipy.linalg

# remember x is a vector
def f(x):
    x1 = x[0]
    x2 = x[1]

    f1 = 2.0 * np.exp(x1 * x2) - 2.0*x2