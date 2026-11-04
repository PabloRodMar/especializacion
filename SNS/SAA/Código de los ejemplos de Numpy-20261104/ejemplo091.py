import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
np.save('datos', a)           # crea datos.npy (la extensión se añade sola)

b = np.load('datos.npy')
print(b)                      # [1 2 3 4 5 6]