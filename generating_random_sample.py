import random

population =list(range(1,101))
sample =random.sample(population,10)
sample_mean = sum(sample)/len(sample)

print("sample:",sample)
print("sample mean:",sample_mean)