import numpy as np
from sklearn.linear_model import LinearRegression
X=np.array([
    [2,70],
    [3,75],
    [4,80],
    [5,85],
    [6,90]
])
Y=np.array([50,55,60,70,75])
model=LinearRegression()
model.fit(X,Y)

print("slope: ",model.coef_)
print("intercept: ",model.intercept_)