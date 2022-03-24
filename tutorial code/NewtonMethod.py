# -*- coding: utf-8 -*-
"""
Script for implementing Newton's method 
using function 'NewtonIteration' defined in Newton.py

"""

import numpy as np
# import function NewtonIteration defined in file Newton.py:
from Newton import NewtonIteration  
#  NewtonIteration has as inputs: function handle f, function handle df (derivative of f)
# initial guess of solution x0, , maximal number of iterations k_max, 
a = 5.0
# tolerance for the error and residual eps_x and eps_f

#  put function definition of f here
def f(x):
    return pow(x, 2) - a

#  put function definition of df here (derivative of f)
def df(x):
    return 2*x
#  assign parameter values
k_max = 20
x0 = 3.0
eps_x = 1e-10
eps_f = 1e-10

#  call NewtonIteration
x, error, residual, convergence = NewtonIteration(f, df, x0, k_max, eps_x, eps_f)

#  print out solution
