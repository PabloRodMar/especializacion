import numpy as np

una_dim = np.array([1, 5, 2, 0])               # como una lista
dos_dim = np.array([[1, 5, 2, 0],
                    [8, 3, 6, 1],
                    [1, 7, 2, 9]])             # como una tabla
tres_dim = np.array([dos_dim, dos_dim * 5])   # como una pila de tablas

print(una_dim.ndim, una_dim.shape) 
print(una_dim)
print('----')

print(dos_dim.ndim, dos_dim.shape)
print(dos_dim)
print('----')

print(tres_dim.ndim, tres_dim.shape) 
print(tres_dim)
