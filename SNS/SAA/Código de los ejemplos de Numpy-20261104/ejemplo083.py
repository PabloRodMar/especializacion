import numpy as np

data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

print(data[0, 1])       # 2
print(data[1:3])        # [[3 4] [5 6]]   -> filas 1 y 2
print(data[0:2, 0])     # [1 3]           -> primera columna de las filas 0 y 1
print(data[:, 1])       # [2 4 6]         -> segunda columna

print(data.max(), data.min(), data.sum())   # 6 1 21

d = np.array([[1, 2],
              [5, 3],
              [4, 6]])
print(d.max(axis=0))    # [5 6]     -> máximo de cada columna
print(d.max(axis=1))    # [2 5 6]   -> máximo de cada fila

ones = np.array([[1, 1], [1, 1]])
m = np.array([[1, 2], [3, 4]])

print(m + ones)      # [[2 3] [4 5]]
print(m * m)         # [[ 1  4] [ 9 16]]   -> elemento a elemento
print(m @ m)         # [[ 7 10] [15 22]]   -> producto matricial

print(data + np.array([[1, 1]]))   # (3, 2) + (1, 2)
# [[2 3]
#  [4 5]
#  [6 7]]

print(np.ones((2, 3, 2)))
# [[[1. 1.]
#   [1. 1.]
#   [1. 1.]]
#
#  [[1. 1.]
#   [1. 1.]
#   [1. 1.]]]

print(np.ones(3), np.zeros(3))      # [1. 1. 1.] [0. 0. 0.]
print(np.ones((3, 2)))              # matriz de 3 filas y 2 columnas de unos
print(np.zeros((3, 2)))             # ... y de ceros

rng = np.random.default_rng(0)
print(rng.random(3))                # [0.63696169 0.26978671 0.04097352]
print(rng.random((3, 2)))
# [[0.01652764 0.81327024]
#  [0.91275558 0.60663578]
#  [0.72949656 0.54362499]]