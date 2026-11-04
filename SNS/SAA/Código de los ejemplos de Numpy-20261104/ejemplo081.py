import numpy as np

data = np.array([1.0, 2.0])
print(data * 1.6)                  # [1.6 3.2]

precios = np.array([10.0, 25.5, 8.0])
print(precios * 1.21)              # [12.1   30.855  9.68 ]   -> precio con IVA

m = np.array([[1, 2],
              [3, 4],
              [5, 6]])                         # forma (3, 2)

print(m + np.array([[10, 20]]))                # fila (1, 2) se repite en las 3 filas
print(m + np.array([10, 20]))                  # un 1-D (2,) funciona igual
# [[11 22]
#  [13 24]
#  [15 26]]

print(m + np.array([[100], [200], [300]]))     # columna (3, 1) se repite en las 2 columnas

np.ones((3, 2)) + np.ones(3)
# ValueError: operands could not be broadcast together with shapes (3,2) (3,)

X = np.array([[1., 2.],
              [3., 6.],
              [5., 10.]])

print(X.mean(axis=0))          # [3. 6.]
print(X - X.mean(axis=0))      # (3, 2) - (2,)  -> broadcasting
