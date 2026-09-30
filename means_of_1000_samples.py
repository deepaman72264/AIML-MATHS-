import random
population=list(range(1,101))
population_mean=sum(population)/len(population)

sample_means=[]

for i in range(1000):
    sample=random.sample(population,10)
    sample_mean=sum(sample)/len(sample)
    sample_means.append(sample_mean)

    average_of_sample_means=sum(sample_means)/len(sample_means)

    print("population mean:",population_mean)
    print("average of sample means:",average_of_sample_means)