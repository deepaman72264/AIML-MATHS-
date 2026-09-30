import numpy as np
data=np.array([2,3,4,5,6])
mean=np.mean(data)
lambda_mle=1/mean

print("mean: ",mean)
print("MLE of lambda: ",lambda_mle)