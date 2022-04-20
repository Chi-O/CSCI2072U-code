"""
in-class example of interpolation

03/18/2022
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
# using barycentric interpolant
from scipy.interpolate import BarycentricInterpolator

x = np.linspace(0, 10, 11)
y = np.cos(-pow(x,2) / 9.0)# function to interpolate

f = interp1d(x,y, 'cubic') # doing piece-wise interpolation, returns a function
# f = interp1d(x,y, 'cubic') # doing piece-wise interpolation, returns a function
fb = BarycentricInterpolator(x,y)

# print(f(0.6783)) # evaluate the function at this point

xx = np.linspace(0, 10, 100)
yy = f(xx)
yy2 = np.cos(-pow(xx,2) / 9.0)

plt.plot(x, y, 'o', xx, yy, 'm', xx, fb(xx), 'c')
plt.legend(["actual points", "interp", "bary"])
plt.show()