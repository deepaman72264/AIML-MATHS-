x=3
delta_x=0.001

y1=x**2
y2=(x+delta_x)**2
derivative=(y2-y1)/delta_x

print("approximate derivative: ",derivative)