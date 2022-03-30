# least-squares approximation

import numpy as np 
import scipy.linalg
import matplotlib.pyplot as plt

# build the matrix for the linear system (refer to last slide of lecture 16)
def LS_Matrix(xd):
    N = xd.shape[0]

    V = np.zeros((N, 2))

    V[:, 0] = np.ones(N) # first column is all 1s
    V[:, 1] = xd 

    print(V.shape)

    return V


# the data  
xd = np.array([0.1, 0.9, 1.3, 2.1, 2.6, 3.1, 4.0])
yd = np.array([0.88, 1.08, 1.37, 1.5, 1.63, 1.91, 2.02])

# get the matrix, i.e. the overdetermined sysrem is V a = yd 
V = LS_Matrix(xd)

# # compute matrices for the normal equations
# M = V.T @ V
# c = V.T @ yd

# # solve for the coefficients, i.e. solving V^T V a = V^T yd
# xstar = scipy.linalg.solve(M, c)

# USING SCIPY
xstar, res, rnk, s = scipy.linalg.lstsq(V, yd) # replaces lines 29, 30, 33


# for plotting interpolant
xx = np.linspace(0.1, 4, 100)
print(xstar)
yy = xstar[0] + xstar[1] * xx

# plot data
plt.plot(xd, yd, 'oc', xx, yy, 'coral')
plt.legend(["data", "least squares approx."])
plt.show()