import numpy as np
from sklearn.linear_model import LinearRegression

X=np.array([
    [2,70,5],
    [3,75,6],
    [4,80,6],
    [5,85,7],
    [6,90,8]
])
Y=np.array([50,55,60,70,75])
model=LinearRegression()
model.fit(X,Y)

prediction=model.predict([[7,95,9]])

print("predicted marks: ",prediction)
print("slope: ",model.coef_)
print("intercept: ",model.intercept_)