import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x=np.array([
    [2,70],
    [3,75],
    [4,80],
    [5,85],
    [6,90]
])
y=np.array([50,55,60,70,75])
model=LinearRegression()
model.fit(x,y)

prediction=model.predict(x)

r2=r2_score(y,prediction)

print("value of r-squared is : ",r2)