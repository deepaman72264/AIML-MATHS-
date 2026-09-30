#let's take an example of time studied vs marks get

import numpy as np
hours=[4,5,6,7,8]
marks=[60,70,80,90,100]

covariance=np.cov(hours,marks)[0][1]

print("covariance between hours studied and marks obtained are:",covariance)