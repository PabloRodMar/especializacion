import pandas as pd

# analizando datos con Pandas

# VIENDO LOS DATOS

# CABECERA - head()

# Uno de los métodos más utilizados para obtener una visión 
# general rápida del DataFrame es el método head().

# El método head() devuelve las cabeceras y un número determinado 
# de filas, empezando por la primera.

# df = pd.read_csv('data.csv')
# print(df.head(10))

# si no se indica número en el head por defecto es 5

# df = pd.read_csv('data.csv')
# print(df.head())

 # FINAL -- tail()

# df = pd.read_csv('data.csv')
# print(df.tail(10))

# si no se indica número en el head por defecto es 5

# df = pd.read_csv('data.csv')
# print(df.tail())

# INFORMACIÓN DEL DATAFRAME -- info()

# El objeto DataFrames dispone de un método llamado info(), 
# que te proporciona más información sobre el conjunto de datos.

df = pd.read_csv('data.csv')
print(df.info()) 

# explicando el resultado

# El resultado dice que hay  169 filas (de la 0 a la 168) y 4 columnas

# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns)

# también muestra el nombre de cada columna y su tipo de dato

# #  Column  Non-Null Count Dtype  
# 0 Duration  169 non-null  int64
# 1 Pulse     169 non-null  int64
# 2 Maxpulse  169 non-null  int64
# 3 Calories  164 non-null  int64

# VALORES NULOS

# El método info() también nos indica cuántos valores no nulos hay en cada columna, 
# y en nuestro conjunto de datos parece que hay 164 de 169 valores no nulos en la 
# columna «Calorías».

# Esto significa que hay 5 filas sin ningún valor en la columna «Calorías», 
# por la razón que sea.

# Los valores vacíos, o valores nulos, pueden ser un problema a la hora 
# de analizar datos, por lo que deberías plantearte eliminar las filas 
# con valores vacíos. Este es un paso hacia lo que se conoce como limpieza de datos.
