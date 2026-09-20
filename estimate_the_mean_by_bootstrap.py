import numpy as np
data=[10,20,30,40,50]
bootstrap_means=[]
for i in range(1000):
    sample=np.random.choice(data,size=len(data),replace=True)
    mean=np.mean(sample)
    bootstrap_means.append(mean)

print("original mean:",np.mean(data))
print("bootstreap mean:",np.mean(bootstrap_means))