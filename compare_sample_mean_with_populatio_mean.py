import random
population = list(range(1,101))
population_mean =sum(population)/len(population)

for i in range(5):
    sample =random.sample(population,10)
    sample_mean=sum(sample)/len(sample)
    print("sample mean:",sample_mean)

    print("population mean:",population_mean)

