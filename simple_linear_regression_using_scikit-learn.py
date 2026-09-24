import numpy as np
from sklearn.linear_model import LinearRegression

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([2,4,6,8,10])

model=LinearRegression()
model.fit(x,y)

prediction=model.predict([[6]])

print("prediction at x=6:",prediction[0])
print("slope:",model.coef_[0])
print("intercept:",model.intercept_)