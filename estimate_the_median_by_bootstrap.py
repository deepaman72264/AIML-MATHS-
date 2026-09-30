import numpy as np
data=[10,12,15,18,20,25,30]
bootstrap_medians=[]

for i in range(1000):
    sample=np.random.choice(data,size=len(data),replace=True)
    bootstrap_medians.append(np.median(sample))

lower=np.percentile(bootstrap_medians,2.5)
upper=np.percentile(bootstrap_medians,97.5)

print("original median:",np.median(data))
print("95% bootstrap class interval:",lower,"to",upper)