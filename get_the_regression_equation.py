import numpy as np
from sklearn.linear_model import LinearRegression

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([5,10,15,20,25])

model=LinearRegression()
model.fit(x,y)

slope=model.coef_[0]
intercept=model.intercept_

print("slope:",slope)
print("intercept:",intercept)

print("regression equation:")
print("y=",slope,"x+",intercept)