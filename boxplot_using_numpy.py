import numpy as np
import matplotlib.pyplot as plt
data= np.random.randint(40,101,50)
plt.boxplot(data)

plt.title("random student marks")
plt.ylabel("marks")

plt.show()