import numpy as np

x = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print(x.flatten())        # [ 1  2  3  4  5  6  7  8  9 10 11 12]

a1 = x.flatten()
a1[0] = 99
print(x[0, 0], a1[0])     # 1 99   -> el original sigue igual

a2 = x.ravel()
a2[0] = 98
print(x[0, 0], a2[0])     # 98 98   -> el original también cambió

print(np.shares_memory(x, a1))   # False  (flatten: copia)
print(np.shares_memory(x, a2))   # True   (ravel: vista)