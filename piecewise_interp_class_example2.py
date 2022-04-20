"""
example of piece-wise polynomial interpolation

>> a different method of gdoing cubic spline interpolant

25/03/2022
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import UnivariateSpline

# data points
x = np.linspace(0, 10, 11)
y = np.cos(-x**2/9.0)

# points for plotting interpolant
xx = np.linspace(0, 10, 1000)

yy = np.cos(-(xx)**2/9.0)

# also cubic interpolation
f_uni = UnivariateSpline(x, y, k=3, s=0)  # k=3 -> cubic, k=2 -> quadratic
fd1 = f_uni.derivative() # compute the first derivative of the cubic spline
fd2 = fd1.derivative()
fd3 = fd2.derivative()

plt.plot(x, y, 'om', xx, f_uni(xx), 'green', xx, fd1(xx), 'blue', xx, fd2(xx), 'orange', xx, fd3(xx), 'pink')
plt.legend(["data", "cubic", "first derivative", "second derivate", "third derivative"])
plt.show()
