import math
def statistic(data):
    mean=sum(data)/len(data)
    variance=sum((x-mean)**2 for x in data)/len(data)
    sd=math.sqrt(variance)

    print("mean:",mean)
    print("variance:",variance)
    print("standard deviation:",sd)

marks=[80,90,100,120,140]
statistic(marks)