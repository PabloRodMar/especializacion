import duckdb

conexion = duckdb.connect()

conexion.execute("""
    CREATE VIEW eventos AS
    SELECT *
    FROM read_parquet(
        'CURATED/fecha=*/*.parquet',
        hive_partitioning = true
    )
""")

resultado = conexion.execute("""
    SELECT COUNT(*) AS total_eventos
    FROM eventos
""").df()

print(resultado)

# # Consulta 2: eventos por fecha
# resultado = conexion.execute("""
#     SELECT fecha, COUNT(*) AS total_eventos
#     FROM eventos
#     GROUP BY fecha
#     ORDER BY fecha
# """).df()

# print(resultado)

# # Consulta 3: temperaturas por fecha
# resultado = conexion.execute("""
#     SELECT fecha,
#         MIN(temperature_c) AS temp_min,
#         AVG(temperature_c) AS temp_media,
#         MAX(temperature_c) AS temp_max
#     FROM eventos
#     WHERE temperature_c IS NOT NULL
#     GROUP BY fecha
#     ORDER BY fecha
# """).df()

# print(resultado)

# # Consulta 4: aperturas de puerta por sensor
# resultado = conexion.execute("""
#     SELECT sensor_id, COUNT_IF(door_open) AS aperturas
#     FROM eventos
#     GROUP BY sensor_id
#     ORDER BY aperturas DESC
# """).df()

# print(resultado)

# # Consulta 5: estado de las baterías
# resultado = conexion.execute("""
#     SELECT sensor_id,
#         COUNT_IF(battery_percent < 20) AS bateria_baja,
#         COUNT_IF(battery_percent IS NULL) AS bateria_no_informada
#     FROM eventos
#     GROUP BY sensor_id
#     ORDER BY bateria_baja, sensor_id
# """).df()

# print(resultado)

# Consulta 6: análisis del 15 de octubre
resultado = conexion.execute("""
    SELECT fecha,
        COUNT(*) AS total_eventos,
        AVG(temperature_c) AS temp_media
    FROM eventos
    WHERE fecha = '2026-10-15'
    GROUP BY fecha
""").df()

print(resultado)