"""
in-class example of interpolation

03/19/2022
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 10, 11)
y = np.cos(-pow(x,2) / 9.0)# function to interpolate

# f = interp1d(x,y) # doing piece-wise interpolation, returns a function
f = interp1d(x,y, 'cubic') # doing piece-wise interpolation, returns a function

# print(f(0.6783)) # evaluate the function at this point

xx = np.linspace(0, 10, 100)
yy = f(xx)
yy2 = np.cos(-pow(xx,2) / 9.0)

plt.plot(x, y, 'o', xx, yy, 'm', xx, yy2, 'c')
plt.legend(["actual points", "inter", "actual line"])
plt.show()