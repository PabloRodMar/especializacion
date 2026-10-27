import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))

a = np.array((1, 2, 3, 4))
b = np.array([1, 2, 3, 4])
c= np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr1, type(arr1))
# print(arr2, type(arr2))
# print(arr3, type(arr3))
# print(arr4, type(arr4))

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print("Número de dimensiones: ",arr.ndim)

qwe

# arr = np.array([1, 2, 3, 4])
# print(arr[0])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Segundo elemento en la primera fila: ", arr[0, 1])
print("Quinto elemento en la segunda fila: ", arr[1, 4])

