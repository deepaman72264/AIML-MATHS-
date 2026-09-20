from statsmodels.stats.power import TTestPower

effect_size=0.5
alpha=0.05
power=0.80

required_sample=TTestPower().solve_power(
    effect_size=effect_size,
    alpha=alpha,
    power=power,
    alternative="two-sided"
)
print("required sample size:",required_sample)