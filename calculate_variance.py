sample =[10,20,30,40,50]
mean =sum(sample)/len(sample)

squared_difference=[]

for x in sample:
    difference=x-mean
    squared=(difference)**2
    squared_difference.append(squared)
    variance=sum(squared_difference)/len(sample)

    print("mean:",mean)
    print("variance:",variance)
    

   