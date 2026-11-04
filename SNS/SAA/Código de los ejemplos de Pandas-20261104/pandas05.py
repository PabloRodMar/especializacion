import pandas as pd

# lectura de ficheros .csv in pandas

# Una forma sencilla de almacenar grandes conjuntos de datos 
# es utilizar archivos CSV (archivos separados por comas).

# Los archivos CSV contienen texto sin formato y son un formato 
# muy conocido que puede leer cualquier persona, incluido Pandas.

# En nuestros ejemplos utilizaremos un archivo CSV llamado «datos.csv».


# df = pd.read_csv('datos.csv')
# print(df.to_string())  # escribe en modo texto las líneas del dataframe

# si el dataframe es muy largo

# el print del dataframe muestra las 5 primeras y ultimas líneas del mismo

# df = pd.read_csv('datos.csv')
# print(df) 

# NÚMERO MÁXIMO DE FILAS QUE SE IMPRIMEN DEL DATAFRAME

# para averiguarlo 

# df = pd.read_csv('datos.csv')
# print(pd.options.display.max_rows)

# si el número de filas que contiene el dataframe es mayor 
# al número obtenido se imprime la cabecera y el final

# para cambiar el número

# df = pd.read_csv('datos.csv')
# pd.options.display.max_rows = 9999
# df = pd.read_csv('data.csv')
# print(df)

