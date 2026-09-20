#we'll use the bootstrap to find the 95% confidence level
import numpy as np
sample=[10,12,15,18,20]
bootstrap_means=[]

for i in range(1000):
    bootstrap_sample=np.random.choice(sample,size=len(sample),replace=True)
    bootstrap_means.append(np.mean(bootstrap_sample))

lower=np.percentile(bootstrap_means,2.5)
upper=np.percentile(bootstrap_means,97.5)

print("original mean:",np.mean(sample))
print("95% bootstrap class interval:",lower,"to",upper)
