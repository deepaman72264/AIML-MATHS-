import random
students=[random.randint(0,100) for i in range(1000)]

population_mean=sum(students)/len(students)
sample=random.sample(students,100)
sample_mean=sum(sample)/len(sample)

print("actual population mean:",population_mean)
print("estimated mean:",sample_mean)