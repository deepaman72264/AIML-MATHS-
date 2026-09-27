import numpy as np
heads=7
tails=3

best_p=0
best_likelihood=0

for p in np.arange(0.1,1.0,0.1):
    likelihood=(p**heads)*((1-p)**tails)

    if likelihood>best_likelihood:
        best_likelihood=likelihood
        best_p=p

print("MLE of p: ",best_p)
print("maximum likelihood: ",best_likelihood)