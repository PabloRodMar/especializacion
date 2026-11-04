import numpy as np

data = np.array([10, 20, 30, 40, 50])

print(data[1])       # 20
print(data[0:2])     # [10 20]
print(data[2:])      # [30 40 50]
print(data[-2:])     # [40 50]      -> los dos últimos
print(data[::2])     # [10 30 50]   -> de 2 en 2
print(data[::-1])    # [50 40 30 20 10]

notas = np.array([[5.5, 7.0, 6.5, 8.0],     # alumno 0
                  [4.0, 6.0, 9.0, 7.5],     # alumno 1
                  [8.5, 9.5, 7.0, 10.0]])   # alumno 2

print(notas[1, :])        # [4.  6.  9.  7.5]   -> fila 1 completa
print(notas[:, 2])        # [6.5 9.  7. ]       -> columna 2 completa
print(notas[0:2, 1:3])    # filas 0-1 y columnas 1-2
# [[7.  6.5]
#  [6.  9. ]]


print(notas[notas < 5])                    # [4.]
print(notas[notas >= 9])                   # [ 9.   9.5 10. ]
print(notas[(notas > 6) & (notas < 8)])    # [7.  6.5 7.5 7. ]
print(notas[(notas < 5) | (notas == 10)])  # [ 4. 10.]

print(notas > 7)       # la propia máscara
# [[False False False  True]
#  [False False  True  True]
#  [ True  True False  True]]


aprobados = notas >= 5
print(aprobados.sum())     # 11   -> notas aprobadas
print(aprobados.mean())    # 0.9166666666666666  -> 91,7 %


b = np.nonzero(notas < 6)
print(b)                   # (array([0, 1]), array([0, 0]))
print(notas[b])            # [5.5 4. ]

for coord in zip(b[0], b[1]):      # coordenadas (fila, columna)
    print(tuple(int(c) for c in coord))
# (0, 0)
# (1, 0)

print(np.nonzero(notas == 42))     # (array([], dtype=int64), array([], dtype=int64))