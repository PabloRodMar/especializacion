import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
a[0] = 10
print(a)          
print(a[:3]) 

m = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

print(m[1, 3])    # 8   -> fila 1, columna 3, en un único par de corchetes
print(m[2, 0])    # 9
print(m[1])       # [5 6 7 8]  -> la fila completa