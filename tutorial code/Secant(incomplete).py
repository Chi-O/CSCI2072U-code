
# Python function for Secant iteration

# you'll need to change the inputs
def SecantIteration(f,df,x0, kMax, eps_x, eps_f):  
# Input: list the inputs in this comment
    x=x0                       #  you'll need to change this: you now have 2 initial guesses 
    conv=False                         # flag for convergence
   
    for k in range(1,kMax):
        fx=f(x)                 # current function value
        
        dx=-fx/df(x)            # update step  ->  you'll need to change the update step
        
        err = abs(dx)              # current error estimate
        res = abs(fx)              # current residual       
        print("Iteration "+str(k)+" err="+str(err)+" res="+str(res))        
        if err < eps_x and res < eps_f:       # If converged ...
            print("Converged!")
            conv=True
            break
        x=x+dx
        
        #  you'll need reassign values for the next iteration here
    
    if (conv==False):
        print("No convergence!")
    return x,err,res,conv


