
# Pandas es una librería de Python usada para trabajar con DataSet
# Esta librería tiene funciones para:
# analizar, limpiar, explorar y manipular datos.

# Porqué usar Pndas?

# Pandas nos permite analizar grandes volúmenes de datos y 
# extraer conclusiones basadas en teorías estadísticas.

# Pandas puede depurar conjuntos de datos desordenados y
# hacer que resulten legibles y relevantes.

# Los datos relevantes son muy importantes en la ciencia de datos.

# Ciencia de datos: es una rama de la informática en la que se estudia 
# cómo almacenar, utilizar y analizar datos para extraer información de ellos.

# ¿Qué puede hacer Pandas?

# Pandas te ofrece respuestas sobre los datos. Por ejemplo:

# ¿Existe alguna correlación entre dos o más columnas?
# ¿Cuál es el valor medio?
# ¿El valor máximo?
# ¿El valor mínimo?
# Pandas también es capaz de eliminar filas que no sean relevantes o 
# que contengan valores erróneos, como valores vacíos o NULL. 
# A esto se le denomina «limpieza de datos».

# Instalación

# pip install pandas

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

# creación de DataSet a partir de un diccionario

myvar = pd.DataFrame(mydataset)
print(myvar)
