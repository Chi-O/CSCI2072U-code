
# Python function for Newton iteration

def NewtonIteration(f, df, x0, kMax, eps_x, eps_f):
    # Input: initial point, max nr. of iterations, tolerance for error and residual
    x = x0
    conv = False                         # flag for convergence
    for k in range(1, kMax):
        fx = f(x)                 # current function value
        dx = -fx/df(x)            # update step
        err = abs(dx)              # current error estimate
        res = abs(fx)              # current residual
        print("Iteration "+str(k)+" err="+str(err)+" res="+str(res))
        if err < eps_x and res < eps_f:       # If converged ...
            print("Converged!")
            conv = True
            break
        x = x+dx

    if (conv==False):
        print("No convergence!")
    return x, err, res, conv
