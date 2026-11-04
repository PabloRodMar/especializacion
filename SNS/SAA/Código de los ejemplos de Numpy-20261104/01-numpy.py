import numpy as np

# arr1 = np.array((1, 2, 3, 4, 5))
# arr2 = np.array([1, 2, 3, 4, 5])
# print(arr1)
# print(arr2)


# Access Array Elements
# arr = np.array([1, 2, 3, 4])
# print(arr[0])

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1])
# print('5th element on 2nd row: ', arr[1, 4])

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

# # indices negativos

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('Last element from 2nd dim: ', arr[1, -1])
# print('Last element from 2nd dim: ', arr[-2, -1])

# Slicing arrays

# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].

# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:])

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, 1:4])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 2])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:2, 1:4])

#Data Types in Python

#By default Python have these data types:

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


# Checking the Data Type of an Array

# arr = np.array([1, 2, 3.3, 4])
# print(arr.dtype)

# arr = np.array(['apple', 'banaqwdana', 'cherrypoweri'])
# print(arr.dtype)

# # crear array de un determiando tipo

# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4], dtype='i4')
# print(arr)
# print(arr.dtype)

# Converting Data Type on Existing Arrays

# The best way to change the data type of an existing array, 
# is to make a copy of the array with the astype() method.

# The astype() function creates a copy of the array, 
# and allows you to specify the data type as a parameter.

# The data type can be specified using a string, like 'f' for float, 
# 'i' for integer etc. or you can use the data type directly 
# like float for float and int for integer.

# arr = np.array([1.1, 2.1, 3.8])
# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)

# arr = np.array([1, 0, 3])

# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)

# Shape of an Array
# The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array

# NumPy arrays have an attribute called shape 
# that returns a tuple with each index having 
# the number of corresponding elements.

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('shape of array :', arr.shape)

# What does the shape tuple represent?

# Integers at every index tells about the number of elements 
# the corresponding dimension has.

# In the example above at index-4 we have value 4, so we can say that 
# 5th ( 4 + 1 th) dimension has 4 elements.

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)
# print(newarr)