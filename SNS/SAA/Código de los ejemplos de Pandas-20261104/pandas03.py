# Series en Panda
# Una serie de Pandas es como una columna de una tabla.
# Es una matriz unidimensional que contiene datos de cualquier tipo.

# import pandas as pd

# a = [1, 7, 2]
# myvar = pd.Series(a)
# print(myvar)

# Etiquetas
# Si no se especifica nada más, los valores se etiquetan con su número de índice. 
# El primer valor tiene el índice 0, el segundo el índice 1, etc.

# Esta etiqueta se puede utilizar para acceder a un valor concreto.

# retorna el primer valor de la serie

# print(myvar[0])

# Crear etiquetas
# Con el argumento «index», puedes asignar nombres a tus propias etiquetas.

# import pandas as pd
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)

# Una vez que hayas creado etiquetas, podrás acceder a un elemento 
# haciendo referencia a la etiqueta.

# para saber el elemento de índice 'y'

# print(myvar["y"])

# Objetos clave-valor como Series
# También puedes utilizar un objeto clave-valor, como un diccionario, 
# al crear una Series.

# Crear una Serie Panda a partir de un diccionario

# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# Para seleccionar solo algunas de las entradas del diccionario, 
# utiliza el argumento «index» y especifica únicamente las entradas 
# que quieras incluir en la serie.

# Crea una serie utilizando únicamente los datos de «day1» y «day2»:

# import pandas as pd

# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)

# DataFrames
# Los conjuntos de datos en Pandas suelen ser tablas multidimensionales, 
# denominadas DataFrames.

# Una serie es como una columna, mientras que un DataFrame es la tabla completa.

# Crear un DataFrame a partir de dos Series

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# myvar = pd.DataFrame(data)
# print(myvar)
