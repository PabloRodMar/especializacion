import pandas as pd

# DataFrames de Pandas

# ¿Qué es un DataFrame?

# Un DataFrame de Pandas es una estructura de datos bidimensional, 
# como una matriz bidimensional o una tabla con filas y columnas.

# Crear un simple Pandas DataFrame:

# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

#cargar datos en un objeto DataFrame:
# df = pd.DataFrame(data)
# print(df) 

# Localizar una fila (loc)
# Como se puede observar en el resultado anterior, 
# el DataFrame es como una tabla con filas y columnas.

# Pandas utiliza el atributo «loc» para devolver una o 
# varias filas específicas.

# retornar la fila 0 (referida por el indice)
# print('---')
# print(df.loc[0]) # Retorna una Serie Panda

# Retornar la fila 0 y 1 
# print('---')
# print(df.loc[[0, 1]])       # se usa una lista de índices
                              # retorna un DataFrame

# Índices con nombre
# Con el argumento «index», puedes asignar un nombre 
# a tus propios índices.

# Añade una lista de nombres para asignar un nombre a cada fila:

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df) 

# Utiliza el índice con nombre indicado en el atributo «loc» 
# para devolver la(s) fila(s) especificada(s).

#nos referimos al índice por el nombre:
# print('---')
# print(df.loc["day2"])

# cargar un fichero .csv a un dataframe

# Si tus conjuntos de datos están almacenados en un archivo, 
# Pandas puede cargarlos en un DataFrame.

# en el ejemplo se trata de un fichero .csv con encabezado
# donde los campos están separados por una ','

df = pd.read_csv('data.csv')
print(df)