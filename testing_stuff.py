from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np

data = [[0,0,0],[0,0,0],[1,1,1]]

reversed_data = []
for i in range(len(data)-1, -1, -1):
    reversed_data.append(data[i])


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

minor_ticks = np.arange(0, len(reversed_data), 1)

ax.set_xticks(minor_ticks)
ax.set_yticks(minor_ticks)

ax.grid(b = True)

cmap = colors.ListedColormap(['white','blue'])

plt.pcolormesh(reversed_data, cmap = cmap)
plt.title("Iteration:")
plt.show()
