import numpy as np
x=[1,2,3,4,5]

positive=[2,4,6,8,10]
negative=[10,8,6,4,2]
none=[3,1,5,2,7]

print("positive:",np.corrcoef(x,positive)[0][1])
print("negative:",np.corrcoef(x,negative)[0][1])
print("none:",np.corrcoef(x,none)[0][1])
