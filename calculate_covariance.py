import numpy as np

x=np.array([2,4,6,8,10])
y=np.array([1,3,5,7,9])
n=len(x)

mean_x=np.mean(x)
mean_y=np.mean(y)

covariance=(np.sum((x-mean_x)*(y-mean_y)))/(n-1)

print("covariance:",covariance)