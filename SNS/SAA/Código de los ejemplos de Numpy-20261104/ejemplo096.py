import numpy as np
import pandas as pd

a = np.array([[-2.58289208, 0.43014843],
              [ 0.99027828, 1.17150989]])

df2 = pd.DataFrame(a, columns=['x', 'y'])
print(df2)
#           x         y
# 0 -2.582892  0.430148
# 1  0.990278  1.171510

df2.to_csv('pd.csv', index=False)        # guardar
datos = pd.read_csv('pd.csv').to_numpy() # volver a leer como array

#exportar con el propio NumPy

np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='x,y', comments='')