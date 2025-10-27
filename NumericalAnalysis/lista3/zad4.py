from math import *
def bisection_method(a,b,function,accuracy):
    center = (b+a)/2
    error = abs(function(center))
    if error < accuracy or function(center) == 0:
        return center
    elif function(center) * function(a) < 0:
        return bisection_method(a,center,function,accuracy)
    else:
        return bisection_method(center, b, function,accuracy)

def fun(x):
    return x**4 - log(x + 4)
print(bisection_method(-1.2,-0.8,fun,10**-8))
print(bisection_method(1,1.2,fun,10**-8))
# x = -1.02207, 1.13083 wolfram