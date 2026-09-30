from statsmodels.stats.power import TTestPower

effect_size=0.5
alpha=0.05

for sample_size in [10,20,30,40,50]:
    power=TTestPower().solve_power(
        effect_size=effect_size,
        alpha=alpha,
        nobs=sample_size,
        alternative="two-sided"
    )

print("sample size:",sample_size)
print("power:",power)