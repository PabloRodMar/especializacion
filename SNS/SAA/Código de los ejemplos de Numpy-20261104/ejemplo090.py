import numpy as np

predicciones = np.array([2.5, 0.0, 2.1, 7.8])
etiquetas    = np.array([3.0, -0.5, 2.0, 7.0])

n = len(etiquetas)
error = (1 / n) * np.sum(np.square(predicciones - etiquetas))
print(error)         # 0.2875  (en pantalla: 0.2874999999999999 por el redondeo en coma flotante)

# Al funcionar con operaciones vectorizadas, el código vale igual 
# para 4 valores que para un millón: solo hace falta que ambos arrays
# tengan el mismo tamaño. Se puede abreviar con np.mean, y otras
# métricas se calculan igual:

print(np.mean((predicciones - etiquetas) ** 2))   # MSE  -> 0.2875
print(np.sqrt(error))                             # RMSE -> 0.5361902647381803
print(np.mean(np.abs(predicciones - etiquetas)))  # MAE  -> 0.475
