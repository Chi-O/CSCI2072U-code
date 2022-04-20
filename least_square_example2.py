# least-squares approximation

import numpy as np 
import scipy.linalg
import matplotlib.pyplot as plt

from numpy.random import randn
from numpy.random import seed


# build the matrix for the linear system (refer to last slide of lecture 16)
def LS_Matrix(xd):
    N = xd.shape[0]

    V = np.zeros((N, 3)) # PAY ATTENTION TO THE SIZE OF MATRIX V 

    V[:, 0] = np.ones(N) # first column -> all 1s
    V[:, 1] = xd 
    V[:, 2] = xd*xd  # 3rd column -> x values squared
    # print(V.shape)

    return V


# the data  
N = 10
xd = np.linspace(-1, 2, N) # x values of data points

# choose y data to be along a parabola
y = 1.0 + 2.0*xd - xd*xd # 1 + 2x - x^2

# add noise
seed(1) # gives a seed the to random number generator
yd = 0.3 * randn(N) + y # adds some Gaussian (normal) noise to each data point in y
                        # 0.3 gives the size of noise

# # get the matrix, i.e. the overdetermined sysrem is V a = yd 
V = LS_Matrix(xd)

# # # compute matrices for the normal equations
M = V.T @ V
c = V.T @ yd

# # # solve for the coefficients, i.e. solving V^T V a = V^T yd
xstar = scipy.linalg.solve(M, c)
print("coefficients:\n", xstar)


# # for plotting interpolant
xx = np.linspace(-1, 2, 100)
yy = xstar[0] + xstar[1] * xx + xstar[2]*xx*xx # third column

# plot data
plt.plot(xd, yd, 'oc', xx, yy, 'coral')
plt.legend(["data", "least squares approx."])
plt.show()