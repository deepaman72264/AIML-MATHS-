#calculating the 95% confidence interval given population standard deviation is 5 and the value of z will be 1.96
#let's start CL=mean+(z*(sd/sqrt(n)))

import math
data=[60,65,72,81,93,74,58,69,81,89]
population_sd= 5
z=1.96
n=len(data)

mean=sum(data)/len(data)

standard_error=population_sd/math.sqrt(n)

marginal_error=z*standard_error

lower=mean-marginal_error
upper=mean+marginal_error

print("mean of the data:",mean)
print("upper bound of CL:",upper)
print("lower bound of CL:",lower)