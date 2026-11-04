import numpy as np

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])

print(np.unique(a))
# [11 12 13 14 15 16 17 18 19 20]

valores, indices = np.unique(a, return_index=True)
print(indices)       # [ 0  2  3  4  5  6  7 12 13 14]

valores, cuentas = np.unique(a, return_counts=True)
print(cuentas)       # [3 2 2 2 1 1 1 1 1 1]
print(dict(zip(valores.tolist(), cuentas.tolist())))
# {11: 3, 12: 2, 13: 2, 14: 2, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1}

votos = np.array(["A", "B", "A", "C", "B", "A"])
valores, cuentas = np.unique(votos, return_counts=True)
print(valores, cuentas)     # ['A' 'B' 'C'] [3 2 1]

a_2d = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [1, 2, 3, 4]])      # la última fila repite la primera

print(np.unique(a_2d))               # [ 1  2  3  4  5  6  7  8  9 10 11 12]

print(np.unique(a_2d, axis=0))       # filas únicas
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

filas, indices, cuentas = np.unique(a_2d, axis=0, return_counts=True, return_index=True)
print(indices)    # [0 1 2]
print(cuentas)    # [2 1 1]   -> la primera fila aparece 2 veces

print(np.unique(np.array([[1, 1, 2], [3, 3, 4]]), axis=1))   # columnas únicas
# [[1 2]
#  [3 4]]