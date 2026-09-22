import numpy as np
x=[1,2,3,4,5]

y_positive=[2,4,6,8,10]
y_negative=[10,8,6,4,2]

cov_positive=np.cov(x,y_positive)[0][1]
cov_negative=np.cov(x,y_negative)[0][1]

print("positive covariance:",cov_positive)
print("negative covariance:",cov_negative)