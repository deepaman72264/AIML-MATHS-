import numpy as np
data=np.array([52,54,48,55,51,53,49,56,52,54])
null_mean=50
observed_mean=np.mean(data)
alpha=0.05

#shift the observed mean towards our null mean so that we can assume that our null mean is true for all samples
null_data=data-observed_mean+null_mean
bootstrap_mean=[]

for i in range(10000):
    sample=np.random.choice(null_data,size=len(null_data),replace=True)
    bootstrap_mean.append(np.mean(sample))

bootstrap_means=np.array(bootstrap_mean)   #converting the list into array list , easier to do calculations

#two sided test
difference=abs(observed_mean-null_mean)    #absolute(abs):works like mod in maths, always give poitive value
extreme_level=np.abs(bootstrap_means-null_mean)>=difference
p_value=np.mean(extreme_level)

print("observed mean:",np.mean(data))
print("p-values:",p_value)

if p_value<alpha:
    print("reject the null hypothesis")
else:
    print("not enought evidence to reject the null hypothesis")
