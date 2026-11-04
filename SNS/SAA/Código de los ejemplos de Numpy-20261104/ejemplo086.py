import numpy as np

arr = np.arange(6).reshape((2, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]]

print(arr.transpose())
print(arr.T)           # equivalente
# [[0 3]
#  [1 4]
#  [2 5]]

t3 = np.arange(24).reshape(2, 3, 4)
print(t3.shape)                    # (2, 3, 4)
print(t3.transpose(1, 0, 2).shape) # (3, 2, 4)  -> se intercambian los ejes 0 y 1
print(t3.T.shape)                  # (4, 3, 2)  -> se invierte el orden de todos los ejes

t3 = np.arange(24).reshape(2, 3, 4)
print(t3.shape)                    # (2, 3, 4)
print(t3.transpose(1, 0, 2).shape) # (3, 2, 4)  -> se intercambian los ejes 0 y 1
print(t3.T.shape)                  # (4, 3, 2)  -> se invierte el orden de todos los ejes

data = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

print(data.reshape(2, 3))
# [[1 2 3]
#  [4 5 6]]

print(data.reshape(6))             # [1 2 3 4 5 6]
print(data.reshape(-1, 1).shape)   # (6, 1)  -> una columna


print(data.T)           # [[1 3 5] [2 4 6]]   -> transpuesta
print(data.reshape(2, 3))  # [[1 2 3] [4 5 6]]  -> remodelada: orden distinto


x = np.array([1.2, 3.4, 5.6, 7.8])
print(x.reshape(-1, 1))
# [[1.2]
#  [3.4]
#  [5.6]
#  [7.8]]       forma (4, 1)