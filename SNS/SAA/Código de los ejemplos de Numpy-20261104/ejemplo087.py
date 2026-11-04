import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
revertido = np.flip(arr)
print('Array invertido:', revertido)   # [8 7 6 5 4 3 2 1]
print(arr[::-1])                       # equivalente con slicing

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print(np.flip(arr_2d))           # filas y columnas a la vez
# [[12 11 10  9]
#  [ 8  7  6  5]
#  [ 4  3  2  1]]

print(np.flip(arr_2d, axis=0))   # solo el orden de las filas (de arriba abajo)
# [[ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

print(np.flip(arr_2d, axis=1))   # solo el orden de las columnas (de izquierda a derecha)
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]]

arr_2d[1] = np.flip(arr_2d[1])          # fila de índice 1
print(arr_2d)
# [[ 1  2  3  4]
#  [ 8  7  6  5]
#  [ 9 10 11 12]]

arr_2d[:, 1] = np.flip(arr_2d[:, 1])    # columna de índice 1
print(arr_2d)
# [[ 1 10  3  4]
#  [ 8  7  6  5]
#  [ 9  2 11 12]]