import numpy as np

rng = np.random.default_rng(42)     # semilla fija

print(rng.random(3))                        # decimales en [0, 1)
# [0.77395605 0.43887844 0.85859792]

print(rng.integers(5, size=(2, 4)))         # enteros de 0 a 4 en una matriz 2 x 4
# [[0 3 1 0]
#  [2 4 3 3]]

print(rng.integers(1, 7, size=10))          # 10 tiradas de dado (1 a 6)
# [5 5 4 1 6 3 4 3 2 6]

print(rng.integers(1, 6, size=5, endpoint=True))   # con endpoint=True el 6 también entra
# [5 4 3 5 4]

r1 = np.random.default_rng(7).random(3)
r2 = np.random.default_rng(7).random(3)
print(r1, np.array_equal(r1, r2))    # [0.62509547 0.8972138  0.77568569] True

rng = np.random.default_rng(1)
print(rng.normal(loc=0, scale=1, size=4))        # distribución normal
# [ 0.34558419  0.82161814  0.33043708 -1.30315723]

print(rng.choice(["a", "b", "c"], size=5))       # muestreo con reposición
# ['a' 'a' 'c' 'b' 'a']

datos = np.arange(10)
idx = np.random.default_rng(3).permutation(10)   # orden aleatorio de los índices
print(idx)                                       # [9 6 0 2 1 4 7 5 3 8]

entrenamiento = datos[idx[:8]]
prueba = datos[idx[8:]]
print(entrenamiento, prueba)    # [9 6 0 2 1 4 7 5] [3 8]