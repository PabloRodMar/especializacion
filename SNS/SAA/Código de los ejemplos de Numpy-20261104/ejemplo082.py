import numpy as np

data = np.array([1, 2, 3])
print(data.max())    # 3
print(data.min())    # 1
print(data.sum())    # 6
print(data.mean())   # 2.0
print(data.prod())   # 6
print(data.std())    # 0.816496580927726

t = np.array([[21.5, 19.0, 23.0, 20.5],    # ciudad A
              [18.0, 17.5, 22.0, 19.5],    # ciudad B
              [25.0, 24.5, 27.0, 26.0]])   # ciudad C

print(t.sum())              # 263.5
print(t.min())              # 17.5
print(t.max())              # 27.0
print(t.mean())             # 21.958333333333332

print(t.min(axis=0))        # [18.  17.5 22.  19.5]   -> mínimo de cada día (columna)
print(t.max(axis=1))        # [23. 22. 27.]           -> máximo de cada ciudad (fila)
print(t.mean(axis=1))       # [21.    19.25  25.625]    -> media de cada ciudad

print(t.argmax())           # 10   -> posición del máximo en el array aplanado
print(t.argmax(axis=1))     # [2 2 2]   -> el día más cálido de cada ciudad
print(np.round(t.std(axis=0), 3))   # [2.858 3.009 2.16  2.858]