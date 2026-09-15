marks= [40,70,80,30,50,300]
marks.sort
try:
    percentile=int(input("enter a percentile (1-99):"))
    if 1<=percentile<=99:
        print("valid percentile")
    else:
        print("invalid percentile")
except ValueError:
    print("please enter number only")

position=(percentile/100)*len(marks)
index=int(position)-1
result=marks[index]

print("sorted marks:",marks)
print("percentile value:",result)

