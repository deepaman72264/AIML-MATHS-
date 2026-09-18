#now we are checking the interval of each confidence level 

import math 
data=[72,34,56,87,94,66,44,83,90,76]
population_sd= 5
mean=sum(data)/len(data)
n=len(data)
standard_error=population_sd*math.sqrt(n)

z_90=1.645
z_95=1.96
z_99=2.576

margin_90=z_90*standard_error
upper_90=mean+margin_90
lower_90=mean-margin_90

margin_95=z_95*standard_error
upper_95=mean+margin_95
lower_95=mean-margin_95

margin_99=z_99*standard_error
upper_99=mean+margin_99
lower_99=mean-margin_99

print(" \n 90 class interval:")
print(lower_90,"to",upper_90)

print(" \n 95 class interval:")
print(lower_95,"to",upper_95)

print(" \n 99 class interval:")
print(lower_99,"to",upper_99)
