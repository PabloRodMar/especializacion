import numpy as np

print(np.array([1, 2.5, 3]))       # [1.  2.5 3. ]  -> todo pasa a float64
print(np.array([1, "dos", 3.0]))   # ['1' 'dos' '3.0']  -> todo pasa a texto

np.array([[1, 2, 3], [4, 5]])      # ValueError: filas de distinta longitud