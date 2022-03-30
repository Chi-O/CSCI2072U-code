import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

# from vander import VanderMatrix
# from vander import MonoPolyEval
#  Newton polynomials for interpolation

import numpy as np

def NewtonPolyBuild(xs):
    
    Np1=xs.shape[0]
    V = np.zeros((Np1,Np1))
    
    for i in range(0,Np1):
        
        V[i,0] = 1
        
        for j in range(1,i+1):
            V[i,j] = V[i,j-1]*(xs[i]-xs[j-1])
    
    return V


def NewtonPolyEval(a,xs,xx):
    
    Np1=xs.shape[0]
    qj = np.ones(xx.shape)
    
    Q=a[0]*qj
    
    for j in range(1,Np1):
        qj = qj*(xx - xs[j-1])
        Q=Q+a[j]*qj
        
    print(Q.shape)
        
    return Q

endpoint = 4
NumIterpPts= 4

x = np.array([1, 2, 3, 4]) # data points x
y = np.array([0.2, 0.4, -0.3, 1.5]) # data points y

#x = np.linspace(0,endpoint,NumIterpPts)
#xx = np.linspace(0, endpoint, num=100, endpoint=True) # x points interval
xx = np.array([1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])
#xk = 1.5

#y = np.sin(x)
#y = np.cos(-x**2/9.0)
# yy2 = np.sin(xx)
#yy2 = np.cos(-xx**2/9.0)


V = NewtonPolyBuild(x)
# V = VanderMatrix(x)
a_coeff = scipy.linalg.solve(V,y)


yy = NewtonPolyEval(a_coeff,x,xx)
# yy = MonoPolyEval(a_coeff,xx)
print(xx, "\n", yy)
#print(xk, "\n", NewtonPolyEval(a_coeff,x,xk))

plt.plot(x, y, 'o',xx,yy, '-b')

plt.legend(['data', 'polynomial interpolant','f(x)'], loc='best')
plt.show()