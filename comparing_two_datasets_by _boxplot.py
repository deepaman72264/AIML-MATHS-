import matplotlib.pyplot as plt
class_A=[40,50,55,60,65,70,75]
class_B=[55,60,65,70,75,80,85]
plt.boxplot([class_A, class_B],tick_labels=["class A", "class B"])

plt.title("comparison between two classes")
plt.ylabel("marks")

plt.show()