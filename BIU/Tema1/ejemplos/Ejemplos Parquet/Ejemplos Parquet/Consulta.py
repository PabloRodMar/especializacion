import duckdb

resultado = duckdb.sql("SELECT AVG(engine_temp_c) AS velocidad_media FROM 'telemetria.parquet'")


print(resultado)