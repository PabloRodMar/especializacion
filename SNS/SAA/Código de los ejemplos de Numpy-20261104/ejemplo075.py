import numpy as np

array_ejemplo = np.arange(24).reshape(2, 3, 4)
print(array_ejemplo)

print(array_ejemplo.ndim)    # 3
print(array_ejemplo.size)    # 24   (2 * 3 * 4)
print(array_ejemplo.shape)   # (2, 3, 4)