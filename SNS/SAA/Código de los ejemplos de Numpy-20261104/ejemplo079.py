import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr1 = a[3:8]
print(arr1)        # [4 5 6 7 8]   -> posiciones 3 a 7

a1 = np.array([[1, 1],
               [2, 2]])
a2 = np.array([[3, 3],
               [4, 4]])

print(np.vstack((a1, a2)))
# [[1 1]
#  [2 2]
#  [3 3]
#  [4 4]]

print(np.hstack((a1, a2)))
# [[1 1 3 3]
#  [2 2 4 4]]

x = np.arange(1, 25).reshape(2, 12)
# [[ 1  2  3  4  5  6  7  8  9 10 11 12]
#  [13 14 15 16 17 18 19 20 21 22 23 24]]

print(np.hsplit(x, 3))        # 3 trozos iguales de 4 columnas
# [array([[ 1,  2,  3,  4], [13, 14, 15, 16]]),
#  array([[ 5,  6,  7,  8], [17, 18, 19, 20]]),
#  array([[ 9, 10, 11, 12], [21, 22, 23, 24]])]

print(np.hsplit(x, (3, 4)))   # cortar tras la columna 3 y tras la 4
# [array([[ 1,  2,  3], [13, 14, 15]]),
#  array([[ 4], [16]]),
#  array([[ 5,  6,  7,  8,  9, 10, 11, 12], [17, 18, 19, 20, 21, 22, 23, 24]])]

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

b1 = a[0, :]          # vista de la primera fila
b1[0] = 99
print(a)
# [[99  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]    -> el original ha cambiado

v = a.view()          # otra vista (copia superficial)
v[1, 0] = -5
print(a[1, 0])        # -5

c = a.copy()
c[2, 3] = 0
print(a[2, 3], c[2, 3])             # 12 0   -> el original no cambia
print(np.shares_memory(a, b1))      # True   -> vista
print(np.shares_memory(a, c))       # False  -> copia