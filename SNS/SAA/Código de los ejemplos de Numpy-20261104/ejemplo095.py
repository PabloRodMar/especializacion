import pandas as pd

num = pd.read_csv('ventas.csv', usecols=['Unidades', 'Precio']).to_numpy()
print(num)
# [[120.    2.5]
#  [300.    0.8]
#  [ 45.   24.9]]
print(num.dtype)           # float64