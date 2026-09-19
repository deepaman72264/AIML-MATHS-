#same as our recent question but in this we are going to compare between two groups 

from scipy import stats
method_1= [72,68,75,71,69,74,77,70,73,76]
method_2= [80,82,78,85,79,84,83]

alpha=0.05

t_statistics,p_value=stats.ttest_ind (method_1,method_2)

print("t-statistics:",t_statistics)
print("p-value:",p_value)

if p_value<alpha:
    print("reject the null hypothesis")
else:
    print("not enough evidence to reject the hpothesis")