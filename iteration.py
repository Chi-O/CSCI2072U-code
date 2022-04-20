def f(x):
    return 3*x - 1

# def f(x):
#     return 0.5*(x + 5/x)

x_0 = 1 # should be given
print("x_0 = 1.0")  

x = x_0
for k in range(1, 4):
    x_k = f(x)
    print("x_" + str(k) + " = " + str(f(x)))

    x = x_k