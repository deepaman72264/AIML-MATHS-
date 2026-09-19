#simple p-value decision
#significence level(alpha): the threshold we set for deciding wether evidence against H0 is strong enough

p_value=0.03
alpha=0.05

if p_value<alpha:
    print("reject the null hypothesis")
else:
    print("not enough evidence to reject the null hypothesis")