import numpy as np

a = np.arange(6)
print(a)                 # [0 1 2 3 4 5]

b = a.reshape(3, 2)
print(b)
# [[0 1]
#  [2 3]
#  [4 5]]

print(a.reshape(2, 3))
# [[0 1 2]
#  [3 4 5]]

print(a.reshape(3, -1).shape)   # (3, 2)   -> el -1 lo calcula NumPy

a.reshape(4, 2)
# ValueError: cannot reshape array of size 6 into shape (4,2)

print(np.reshape(a, shape=(1, 6), order='C'))   # [[0 1 2 3 4 5]]

print(a.reshape(2, 3, order='F'))
# [[0 2 4]
#  [1 3 5]]

b = a.reshape(3, 2)
b[0, 0] = 99
print(a)                 # [99  1  2  3  4  5]   -> el original cambió