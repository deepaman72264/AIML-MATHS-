#testing whether null hypothesis(H0) and alternative hypothesis(H1) is same for the sample

from scipy import stats
scores= [72,68,75,71,69,74,77,70,73,76]
population_mean=70
alpha=0.05

t_statistics,p_value= stats.ttest_1samp(scores,population_mean)

print("t-statistics:",t_statistics)
print("p-value:",p_value)

if p_value<alpha:
    print("reject the null hypothesis")
else:
    print("not enough evidence to reject the null hypothesis")
