import json
from pathlib import Path

from fastavro import parse_schema, writer
from fastavro.validation import validate

# 1. Leer el esquema Avro
with open("telemetria.avsc", "r", encoding="utf-8") as archivo:
    esquema = json.load(archivo)

esquema = parse_schema(esquema)

# 2. Preparar las listas
eventos_validos = []
eventos_descartados = []

# 3. Leer y validar cada evento
with open("telemetria.ndjson", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        evento = json.loads(linea)

        if validate(evento, esquema, raise_errors=False):
            eventos_validos.append(evento)
        else:
            eventos_descartados.append(evento)

# 4. Mostrar el resultado
print("Eventos válidos:", len(eventos_validos))
print("Eventos descartados:", len(eventos_descartados))

# 5. Crear las carpetas
Path("raw").mkdir(exist_ok=True)
Path("descartados").mkdir(exist_ok=True)

# 6. Guardar los eventos válidos en Avro
if eventos_validos:
    with open("raw/telemetria.avro", "wb") as archivo:
        writer(
            archivo,
            esquema,
            eventos_validos,
            codec="deflate"
        )

# 7. Guardar los eventos descartados
if eventos_descartados:
    with open(
        "descartados/eventos_incorrectos.ndjson",
        "w",
        encoding="utf-8"
    ) as archivo:

        for evento in eventos_descartados:
            archivo.write(
                json.dumps(evento, ensure_ascii=False) + "\n"
            )

print("Proceso finalizado")