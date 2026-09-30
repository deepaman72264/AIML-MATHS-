import matplotlib.pyplot as plt
marks=[40,50,55,60,65,70,75,80,90,300]
plt.boxplot(marks)

plt.title("marks with outlier")
plt.ylabel("marks")

plt.show()
