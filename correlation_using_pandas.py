import pandas as pd

data={
    "hours":[4,5,6,7,8],
    "marks":[60,70,80,90,100]
}

df=pd.DataFrame(data)
correlation=df["hours"].corr(df["marks"])
print("correlation:",correlation)