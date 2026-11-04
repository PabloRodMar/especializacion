import numpy as np
import math

# Ventas de 3 tiendas (filas) durante 4 trimestres (columnas)
ventas = np.array([[120, 135, 150, 160],
                   [ 90, 100, 110,  95],
                   [200, 210, 190, 220]])

print(ventas.ndim)    # 2
print(ventas.shape)   # (3, 4)
print(ventas.size)    # 12
print(ventas.dtype)   # int64

print(len(ventas.shape) == ventas.ndim)      # True
print(ventas.size == math.prod(ventas.shape))  # True  (3 * 4 = 12)

f = np.array([1.5, 2.0, 3.25])
print(f.dtype, f.ndim, f.shape, f.size)   # float64 1 (3,) 3