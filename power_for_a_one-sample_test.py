from statsmodels.stats.power import TTestPower

effect_size=0.5
alpha=0.05
sample_size=30

power=TTestPower().solve_power(
    effect_size=effect_size,
    nobs=sample_size,
    alpha=alpha,
    alternative="two-sided"
)

print("statistical power:",power)