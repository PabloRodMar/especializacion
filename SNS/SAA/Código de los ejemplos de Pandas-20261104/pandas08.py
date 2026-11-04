import pandas as pd

# LIMPIEZA DE DATOS

# La limpieza de datos consiste en corregir los datos erróneos 
# de tu conjunto de datos.

# Los datos erróneos pueden ser:

# Celdas vacías
# Datos con un formato incorrecto
# Datos erróneos
# Duplicados

# para trabajar usaremos el fichero datos_analisis.csv

df = pd.read_csv('datos_analisis.csv')
print(df)

# El conjunto de datos contiene algunas celdas vacías 
# («Fecha» en la fila 22 y «Calorías» en las filas 18 y 28).

# El conjunto de datos contiene un formato incorrecto 
# («Fecha» en la fila 26).

# El conjunto de datos contiene datos incorrectos 
# («Duración» en la fila 7).

# El conjunto de datos contiene duplicados 
# (filas 11 y 12).

# LIMPIANDO CELDAS VACIAS

# Celdas vacías
# Las celdas vacías pueden dar lugar a un resultado erróneo 
# al analizar los datos.

# ELIMINAR FILAS .dropna()

# Una forma de gestionar las celdas vacías es eliminar las filas 
# que contienen celdas vacías.

# Esto suele ser adecuado, ya que los conjuntos de datos pueden
# ser muy grandes y eliminar unas pocas filas no tendrá un gran
# impacto en el resultado.

# df = pd.read_csv('datos_analisis.csv')
# new_df = df.dropna()
# print(new_df.to_string())

#Por defecto, el método dropna() devuelve un nuevo DataFrame 
# y no modifica el original.

# Si quieres modificar el DataFrame original, 
# utiliza el argumento 'inplace = True':

# df = pd.read_csv('datos_analisis.csv')
# df.dropna(inplace = True)
# print(df.to_string())

# Ahora bien, la función dropna(inplace = True) NO devolverá 
# un nuevo DataFrame, sino que eliminará todas las filas que 
# contengan valores NULL del DataFrame original.

# SUSTITUIR VALORES VACÍOS

# Otra forma de gestionar las celdas vacías es insertar
# un nuevo valor en su lugar.
# De esta forma, no es necesario borrar filas enteras solo 
# porque haya algunas celdas vacías.

# La función fillna() nos permite sustituir las celdas vacías 
# por un valor:

df = pd.read_csv('datos_analisis.csv')
df.fillna(130, inplace = True)
print(df.to_string())