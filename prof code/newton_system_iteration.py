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


# Newton-Raphson iteration for systems of nonlinear equations
def NewtSysSolve(f, Df, x0, epsx, epsf, kmax):

    conv = False                                               # Set convergence flag
    err = np.ones(kmax)
    res = np.ones(kmax)

    # Sets starting point as initial guess x0
    x = x0

    # Loop over Newton-Raphson iterates
    for k in range(0, kmax):

        # Compute residual vector
        r_vec = -f(x)
        # Compute residual
        res[k] = scipy.linalg.norm(r_vec, 2)
        # Compute Jacobian
        J = Df(x)

        # solve system J dx = -f
        dx = scipy.linalg.solve(J, r_vec)

        # Estimate of error
        err[k] = scipy.linalg.norm(dx, 2)

        # Print error and residual
        print("Iter. " + str(k) + " err= " +
              str(err[k]) + " res= " + str(res[k]))

        x = x + dx                                             # Apply update step

        if res[k] < epsf and err[k] < epsx:                    # Test for convergence
            conv = True
            its = k+1
            print("Converged, exiting...")
            break

    if conv == False:
        print("No convergece!")
        its = kmax

    return x, err, res, its
