from matplotlib import pyplot as plt
import numpy as np

xvalues, yvalues = np.meshgrid(np.arange(-3, 3.1, 0.1), np.arange(-3, 3.1, 0.1))

vx = 2 * xvalues
vy = yvalues - xvalues

plt.streamplot(xvalues, yvalues, vx, vy)

plt.show()
