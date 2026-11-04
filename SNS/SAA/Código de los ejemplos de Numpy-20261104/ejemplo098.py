import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)

plt.plot(x, np.sin(x), 'purple')      # línea de color
plt.plot(x, np.cos(x), '--')          # línea discontinua
plt.plot(x, np.sin(x), 'o')           # puntos
plt.title("Seno y coseno")
plt.xlabel("x (radianes)")
plt.legend(["seno", "coseno", "puntos"])
plt.show()