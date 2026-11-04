import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)    # dos matrices 2-D con todas las combinaciones
R = np.sqrt(X**2 + Y**2)    # distancia al centro
Z = np.sin(R)               # altura

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()
