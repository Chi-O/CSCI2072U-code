"""
example of piece-wise polynomial interpolation

25/03/2022
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d
from scipy.interpolate import CubicSpline
from scipy.interpolate import PchipInterpolator

# data points
x = np.array([0, 1.2, 1.9, 2.3, 3.2, 4.1])
y = np.array([0, 2.2, 1.1, 3.6, 1.1, 5.1])

# points for plotting interpolant
xx = np.linspace(0, 4.1, 1000)

# piecewise linear interpolation
f_lin = interp1d(x, y)

# cubic spline interpolation
f_cub = CubicSpline(x, y)

# shape-preserving cubic interpolation
f_pchip = PchipInterpolator(x, y)


plt.plot(x, y, 'o', xx, f_lin(xx), '-r', xx, f_cub(xx), '-c', xx, f_pchip(xx), '-m')
plt.legend(["data", "linear", "cubic", "pchip"])
plt.show()