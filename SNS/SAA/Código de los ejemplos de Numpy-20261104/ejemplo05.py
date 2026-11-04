import numpy as np
## Tipo de dato de un array
arr0 = np.array(42)
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10,11, 12]]])
print(arr0, type(arr0))
print('---')
print(arr1, type(arr1))
print('---')
print(arr2, type(arr2))
print('---')
print(arr3, type(arr3))
print('---')
# Check Number of Dimensions?
print('Dimensiones')
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# Higher Dimensional Arrays
#
# An array can have any number of dimensions.

# When the array is created, you can define the number of dimensions 
# by using the ndmin argument.

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)
