import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=np.int_)

print(data + ones)    # [2 3]
print(data - ones)    # [0 1]
print(data * data)    # [1 4]
print(data / data)    # [1. 1.]
print(data ** 2)      # [1 4]

a = np.array([1, 2, 3, 4])
print(a.sum())        # 10
print(np.sum(a))      # 10   -> misma operación como función

b = np.array([[1, 1],
              [2, 2]])
print(b.sum(axis=0))   # [3 3]   -> suma de cada columna
print(b.sum(axis=1))   # [2 4]   -> suma de cada fila
print(b.sum())         # 6       -> todo el array

c = np.array([[1, 2, 3],
              [4, 5, 6]])
print(c.sum(axis=0))   # [5 7 9]
print(c.sum(axis=1))   # [ 6 15]