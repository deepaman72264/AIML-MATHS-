t=3
delta_t=0.001

s1=t**2
s2=(t+delta_t)**2
velocity=(s2-s1)/delta_t

print("approximate velocity: ",velocity)