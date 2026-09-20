from statsmodels.stats.power import TTestPower

alpha=0.05
sample_size=30

for effect_size in [0.2,0.3,0.8,0.5,0.7]:
    power=TTestPower().solve_power(
    effect_size=effect_size,
    alpha=alpha,
    nobs=sample_size,
    alternative="two-sided"
)
print("effect size:",effect_size)
print("power:",power)
