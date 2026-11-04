# Ventas de 3 tiendas (filas) durante 4 trimestres (columnas)
import numpy as np

ventas = np.array([[120, 135, 150, 160],
                   [ 90, 100, 110,  95],
                   [200, 210, 190, 220]])

print(ventas.ndim)    # 2
print(ventas.shape)   # (3, 4)
print(ventas.size)    # 12
print(ventas.dtype)   # int64