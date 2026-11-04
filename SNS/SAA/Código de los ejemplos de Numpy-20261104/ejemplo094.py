
import pandas as pd

df = pd.read_csv('ventas.csv')
print(df)
#     Producto  Unidades  Precio
# 0   Cuaderno       120     2.5
# 1  Bolígrafo       300     0.8
# 2    Mochila        45    24.9

print(df.values)           # array de NumPy; con tipos mezclados es de objetos
# [['Cuaderno' 120 2.5]
#  ['Bolígrafo' 300 0.8]
#  ['Mochila' 45 24.9]]