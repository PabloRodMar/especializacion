import math
import numpy as np

ventas = np.array([[120, 135, 150, 160],
                   [ 90, 100, 110,  95],
                   [200, 210, 190, 220]])

print(len(ventas.shape) == ventas.ndim)      # True
print(ventas.size == math.prod(ventas.shape))  # True  (3 * 4 = 12)

f = np.array([1.5, 2.0, 3.25])
print(f.dtype, f.ndim, f.shape, f.size)   # float64 1 (3,) 3

print(len(ventas.shape) == ventas.ndim)      # True
print(ventas.size == math.prod(ventas.shape))  # True  (3 * 4 = 12)