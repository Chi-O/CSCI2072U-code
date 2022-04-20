"""
09/04/2022

in-class example of composite trapezoidal formula
approximating definite integral using composite trapezoidal
"""

import numpy as np
import matplotlib.pyplot as plt


def comp_trap(f, a, b, M):
    xs = np.linspace(a, b, M+1)  # generate M equally spaced points
    h = (b-a) / float(M)  # calculate h

    I = (f(a) + f(b)) / 2

    for k in range(1, M):
        I += f(xs[k])

    I *= h

    return I


def f(x):
    return np.sqrt(1.0 + pow(x, 4))


a = 0
b = 1

M = 2
Mtest = 17

# let's say this is the exact value
I_final = comp_trap(f, a, b, M**(Mtest+1))

h_all = np.zeros(Mtest - 1)
Err = np.zeros(Mtest - 1)

for j in range(1, Mtest):
    M = M * 2
    I_trap = comp_trap(f, a, b, M)
    print("approximation = " + str(I_trap) + " with " + str(M) + " subintervals")

    h_all[j - 1] = (b-a)/float(M)
    Err[j - 1] = I_trap - I_final


plt.loglog(h_all, Err, 'orange')
plt.xlabel("h")
plt.ylabel("error")
plt.grid(True)
plt.show()