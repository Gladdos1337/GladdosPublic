import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(0, 0, figsize=(5, 5))
axs[1, 1].hist2d(data[0], data[1])

plt.show()