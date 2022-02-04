# bisection code as programmed in lecture 3
# input: function f, starting points a0 and b0, max iteration (k_max), tolerances eps x and eps f

from re import L
import numpy as np
import math


def bisect(f, a0, b0, k_max, eps_x, eps_f):
    # let the user know if it was convergent
    # flag for convergence, default is "not converged"
    conv = False

    a = a0
    b = b0

    for k in range(k_max):
        # find midpoint
        c = (a + b)/2.0

        f_mid = f(c)
        f_left = f(a)

        if (f_mid * f_left) > 0:
            a = c  # set left endpoint to mid
        else:
            b = c

        max_err = abs(b - a)
        residual = abs(f_mid)

        print("iteration %d err = %e and residual = %e" %
              (k + 1, max_err, residual))

        # check whether we should exit
        if (max_err < eps_x) and (residual < eps_f):
            conv = True
            break

    if not conv:
        print("no convergence after %d iterations" % (k_max))

    return c, max_err

# def f(x):
#     return np.exp(-x * x) - x

def f(x):
    return (math.cos(x)) - x

# a0 = 0.0
# b0 = 1.0 
# k_max = 100
# eps_x = 1.0e-5
# eps_f = 1.0

# xstar, err = bisect(f, a0, b0, k_max, eps_x, eps_f)

# print("x = %e" % (xstar))

a0 = 0.0
b0 = 2.0 
k_max = 100
eps_x = 1.0e-4
eps_f = 1.0

xstar, err = bisect(f, a0, b0, k_max, eps_x, eps_f)

print("x = %e" % (xstar))