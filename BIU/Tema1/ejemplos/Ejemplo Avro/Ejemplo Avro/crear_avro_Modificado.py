import json
from pathlib import Path

from fastavro import parse_schema, reader, writer
from fastavro.validation import validate

# 1. Leer el contrato Avro
with open("telemetria.avsc", "r", encoding="utf-8") as archivo:
    esquema = json.load(archivo)

esquema = parse_schema(esquema)

# 2. Preparar las salidas
Path("raw").mkdir(exist_ok=True)
Path("descartados").mkdir(exist_ok=True)

eventos_validos = []
eventos_descartados = []

# 3. Leer y validar cada evento individualmente
with open("telemetria.ndjson", "r", encoding="utf-8") as archivo:
    for numero_linea, linea in enumerate(archivo, start=1):

        try:
            evento = json.loads(linea)

        except json.JSONDecodeError:
            eventos_descartados.append({
                "linea": numero_linea,
                "motivo": "JSON incorrecto",
                "contenido": linea.strip()
            })
            continue

        if validate(evento, esquema, raise_errors=False):
            eventos_validos.append(evento)
        else:
            eventos_descartados.append({
                "linea": numero_linea,
                "motivo": "No cumple el esquema Avro",
                "evento": evento
            })

print("Eventos recibidos:",
      len(eventos_validos) + len(eventos_descartados))

print("Eventos válidos:", len(eventos_validos))
print("Eventos descartados:", len(eventos_descartados))

# 4. Escribir en Avro solamente los eventos válidos
if eventos_validos:
    with open("raw/telemetria.avro", "wb") as archivo:
        writer(
            archivo,
            esquema,
            eventos_validos,
            codec="deflate"
        )

    print("Eventos válidos guardados en raw/telemetria.avro")

# 5. Guardar los eventos incorrectos
if eventos_descartados:
    with open(
        "descartados/eventos_incorrectos.ndjson",
        "w",
        encoding="utf-8"
    ) as archivo:

        for rechazo in eventos_descartados:
            archivo.write(
                json.dumps(rechazo, ensure_ascii=False) + "\n"
            )

    print("Eventos incorrectos guardados en descartados")