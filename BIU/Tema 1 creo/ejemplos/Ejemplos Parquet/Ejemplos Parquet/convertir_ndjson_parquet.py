import pandas as pd
import pyarrow.parquet as pq

# 1. Leer los 6 registros del archivo NDJSON
## Leer el NDJSON y crear automáticamente un DataFrame
df = pd.read_json("telemetria.ndjson", lines=True) #Se indica lines a true pq es un ndjson

print("DATOS ORIGINALES EN NDJSON")
print(df)

# 2. Exportar los datos a Parquet
df.to_parquet(
    "telemetria.parquet",
    engine="pyarrow",
    compression="snappy",
    index=False
)

print("\nArchivo telemetria.parquet creado correctamente")
"""
# 3. Volver a leer el archivo Parquet
df_leido = pd.read_parquet(
    "telemetria.parquet",
    engine="pyarrow"
)

print("\nDATOS RECUPERADOS DESDE PARQUET")
print(df_leido)

# 4. Mostrar la estructura columnar con PyArrow
tabla = pq.read_table("telemetria.parquet")

print("\nESQUEMA DEL ARCHIVO")
print(tabla.schema)

print("\nCOLUMNA speed_kmh")
print(tabla.column("speed_kmh"))

print("\nCOLUMNA engine_temp_c")
print(tabla.column("engine_temp_c"))
"""