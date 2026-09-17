#in this code take the user input for confidence level between  90,95,99 with value of z=1.645,1.96,2.576 respectively

import math 
data=[60,65,72,81,93,74,58,69,81,89]
population_sd=5
n=len(data)
confidence_level=int(input("choose the value of CL 90,95,99:"))

if confidence_level==90:
    z=1.645
elif confidence_level==95:
    z=1.96
elif confidence_level==99:
    z=2.576
else:
    print("not a correct input plz choose the values given above thankyou!!")

mean=sum(data)/len(data)

standard_error=population_sd/math.sqrt(n)

marginal_error=z*standard_error

upper=mean+marginal_error
lower=mean-marginal_error

print("mean of data:",mean)
print("lower bound of CL:",lower)
print("upper bound of CL:",upper)
