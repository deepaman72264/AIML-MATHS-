import math
marks=[10,20,30,40,50]
mean=sum(marks)/len(marks)

squared_difference=[]

for x in marks:
    difference=x-mean
    squared=(difference)**2
    squared_difference.append(squared)
    variance=sum(squared_difference)/len(marks)

    standard_deviation=math.sqrt(variance)

    print("mean:",mean)
    print("variance:",variance)
    print("standad deviation:",standard_deviation)