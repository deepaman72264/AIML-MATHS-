def derivative (f,x,dx=0.00001):
    return(f(x+dx)-f(x)/dx)

def square(x):
    return x**2

def cube(x):
    return x**3

print("derivative of x square at x=3 ",derivative(square,3))
print("derivative of x cube at x=2 ",derivative(cube,2))