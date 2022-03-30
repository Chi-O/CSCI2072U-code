import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg
#from NewtonPolynomial import NewtonPolyBuild
#from NewtonPolynomial import NewtonPolyEval
from vander import VanderMatrix
from vander import MonoPolyEval

endpoint = 4
NumIterpPts= 4

x = np.array([1, 2, 3, 4]) # data points x
y = np.array([0.2, 0.4, -0.3, 1.5]) # data points y

#x = np.linspace(0,endpoint,NumIterpPts)
xx = np.linspace(0, endpoint, num=100, endpoint=True) # x points interval
xk = 1.5

#y = np.sin(x)
#y = np.cos(-x**2/9.0)
# yy2 = np.sin(xx)
#yy2 = np.cos(-xx**2/9.0)


#V = NewtonPolyBuild(x)
V = VanderMatrix(x)
a_coeff = scipy.linalg.solve(V,y)


#yy = NewtonPolyEval(a_coeff,x,xx)
yy = MonoPolyEval(a_coeff,xx)
print(xx, "\n", yy)
print(xk, "\n", MonoPolyEval(a_coeff,xk))

plt.plot(x, y, 'o',xx,yy, '-b')

plt.legend(['data', 'polynomial interpolant','f(x)'], loc='best')
plt.show()