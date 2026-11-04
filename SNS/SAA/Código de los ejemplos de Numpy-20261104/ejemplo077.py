import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape)                      # (6,)

fila = a[np.newaxis, :]             # eje nuevo al principio
print(fila.shape)                   # (1, 6)  -> vector fila

columna = a[:, np.newaxis]          # eje nuevo al final
print(columna.shape)                # (6, 1)  -> vector columna

b = np.expand_dims(a, axis=1)
print(b.shape)                      # (6, 1)

c = np.expand_dims(a, axis=0)
print(c.shape)                      # (1, 6)

m = np.ones((2, 3))
print(m[np.newaxis].shape)          # (1, 2, 3)
print(m[:, np.newaxis, :].shape)    # (2, 1, 3)

col = np.array([1, 2, 3])[:, np.newaxis]     # (3, 1)
fil = np.array([10, 20, 30])[np.newaxis, :]  # (1, 3)
print(col + fil)
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]