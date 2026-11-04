# cargar un fichero .csv en un DataFrame

import pandas as pd

df = pd.read_csv('data.csv')
print(df.to_string())