"""
Compute the piecewise linear interpolant through these data and evaluate it at x = 1.3

08/04/2022
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d


# data points
x = np.array([0.0, 0.4, 0.9, 1.6, 2.0])
y = np.array([0.4, 0.9, 2.3, 1.9, 2.7])

# points for plotting interpolant
xx = np.linspace(0.0, 2.0, 1000)
point_to_eval = 1.3

# piecewise linear interpolation
f_lin = interp1d(x, y)
print(f_lin(point_to_eval))


plt.plot(x, y, 'o', xx, f_lin(xx), '-c')
plt.legend(["data", "linear"])
plt.show()
