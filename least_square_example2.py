# least-squares approximation

import numpy as np 
import scipy.linalg
import matplotlib.pyplot as plt

from numpy.random import randn
from numpy.random import seed


# build the matrix for the linear system (refer to last slide of lecture 16)
def LS_Matrix(xd):
    N = xd.shape[0]

    V = np.zeros((N, 2))

    V[:, 0] = np.ones(N) # first column is all 1s
    V[:, 1] = xd 

    print(V.shape)

    return V


# the data  
N = 10
xd = np.linspace(-1, 2, N)

y = 1.0 + 2.0*xd - xd*xd

# add noise
seed(1) # gives a seed the to random number generator
yd = 0.3 * randn(N) + y # adds some Gaussian (normal) noise to each data point in y
                        # 0.3 gives the size of noise

# # get the matrix, i.e. the overdetermined sysrem is V a = yd 
# V = LS_Matrix(xd)

# # # compute matrices for the normal equations
# M = V.T @ V
# c = V.T @ yd

# # # solve for the coefficients, i.e. solving V^T V a = V^T yd
# xstar = scipy.linalg.solve(M, c)



# # for plotting interpolant
# xx = np.linspace(-1, 2, 100)
# print(xstar)
# yy = xstar[0] + xstar[1] * xx

# plot data
plt.plot(xd, y, 'oc')
plt.legend(["data", "least squares approx."])
plt.show()