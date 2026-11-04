import numpy as np

# csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# np.savetxt('nuevo.csv', csv_arr)
# print(np.loadtxt('nuevo.csv'))      # [1. 2. 3. 4. 5. 6. 7. 8.]   -> vuelve como float

m = np.array([[1.5, 2.5, 3.5],
              [4.5, 5.5, 6.5]])

np.savetxt('matriz.csv', m, delimiter=',', header='a,b,c', fmt='%.1f')
# Contenido del archivo:
# # a,b,c
# 1.5,2.5,3.5
# 4.5,5.5,6.5

print(np.loadtxt('matriz.csv', delimiter=','))    # la cabecera (con #) se ignora
# [[1.5 2.5 3.5]
#  [4.5 5.5 6.5]]

print(np.loadtxt('matriz.csv', delimiter=',', skiprows=1, usecols=(0, 2)))
# [[1.5 3.5]
#  [4.5 6.5]]