import numpy as np

# ordenar array

# arr = np.array([7, 2, 9, 4, 1, 8])
# arr_ord = np.sort(arr)
# print(arr)      
# print(arr_ord)               

# print(np.sort(np.array(["Eva", "Luis", "Ana"])))

# m = np.array([[3, 8, 7],
#               [9, 1, 2]])
# print(np.sort(m, axis=1))   # ordena cada fila
# print('---')
# print(np.sort(m, axis=0))   # ordena cada columna

# notas = np.array([6.5, 9.0, 4.5, 7.5])
# idx = np.argsort(notas)  # retorna los índices del ordenamiento
# print(idx)               # [2 0 3 1]   posiciones de menor a mayor nota
# print(notas[idx])        # [4.5 6.5 7.5 9. ]
# print(idx[::-1])         # invierte el orden

# busca el índice donde se debe insertar
# print(np.searchsorted(np.array([10, 20, 30, 40]), 25))   # 2 

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(np.concatenate((a, b)))        # [1 2 3 4 5 6]

# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6]])
# print(np.concatenate((x, y), axis=0))    # añade una fila

# x = np.array([[1, 2], [3, 4]])
# z = np.array([[7], [8]])
# print(np.concatenate((x, z), axis=1))    # añade una columna

# borrado de elementos de un array

# p = np.array([10, 20, 30, 40, 50])
# q = p[[0, 3, 4]]   # genera nuevo array
# print(p)
# print(q)     
# print(p[p != 30])          # [10 20 40 50]   -> por condición
# print(np.delete(p, 4))     # [10 20 40 50]   -> borrando la posición 2
