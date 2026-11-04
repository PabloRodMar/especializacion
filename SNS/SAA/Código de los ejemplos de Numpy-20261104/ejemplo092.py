import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
x = np.array([1, 2, 3])
y = np.array([[1., 2.], [3., 4.]])
np.savez('varios.npz', x=x, y=y)         # cada array con un nombre

z = np.load('varios.npz')
print(z.files)                # ['x', 'y']
print(z['x'])                 # [1 2 3]
print(z['y'])                 # [[1. 2.] [3. 4.]]

np.savez_compressed('comprimido.npz', a=a)   # igual, pero comprimido