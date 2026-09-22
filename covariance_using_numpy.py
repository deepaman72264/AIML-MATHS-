import numpy as np
x=(2,4,6,8,10)
y=(1,3,5,7,9)

covariance=np.cov(x,y)[0][1]

print("covariance:",covariance)