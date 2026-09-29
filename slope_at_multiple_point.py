def f(x):
    return x**2

dx=0.0001

for x in range(1,6):
    slope=(f(x+dx)-f(x))/dx
    print("x=",x," slope=",slope)