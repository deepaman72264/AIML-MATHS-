data =[12,18,25,22,30,15,45,28,35,50]
data.sort()
percentile=int(input("enter percentile for Q1,Q2,Q3:"))
if percentile==25 or percentile== 50 or percentile== 75: 
    position=(percentile/100)*len(data)
    index=int(position)-1
    result=data[index]
    print("percentile value is:",result)
else:
    print("no need to find the value")

print(data)