"""
example of piece-wise polynomial interpolation
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
from scipy.interpolate import PchipInterpolator
from scipy.interpolate import UnivariateSpline

# data points
#x = np.array([0, 1.2, 1.9, 2.3, 3.2, 4.1])
#y = np.array([0, 2.2, 1.1, 3.6, 1.1, 5.1])
x = np.linspace(0, 10, 11)
y = np.cos(-x**2/9.0)

# points for plotting interpolant
xx = np.linspace(0, 10, 1000)
yy = np.cos(-(xx)**2/9.0)

# piecewise linear interpolation
# f_lin = interp1d(x, y)


# cubic spline interpolation
# f_cub = CubicSpline(x, y)

# f_pchip = PchipInterpolator(x, y)

# also cubic interpolation
f_uni = UnivariateSpline(x, y, k=3, s=0)  # k=3 -> cubic, k=2 -> quadratic
fd1 = f_uni.derivative()
fd2 = fd1.derivative()
fd3 = fd2.derivative()

plt.plot(x, y, 'om', xx, f_uni(xx), xx, fd1(xx), xx, fd2(xx), xx, fd3(xx))
plt.legend(["data", "cubic", "first", "second", "third"])
plt.show()
