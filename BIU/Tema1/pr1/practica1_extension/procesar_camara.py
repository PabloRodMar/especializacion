import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

from fastavro import parse_schema, reader, writer
from fastavro.validation import validate


RUTA_ENTRADA = Path("camara_frio_60000.ndjson")
RUTA_ESQUEMA = Path("camara_frio.avsc")
RUTA_RAW = Path("RAW")
RUTA_RECHAZADOS = Path("RECHAZADOS")

RUTA_RAW.mkdir(exist_ok=True)
RUTA_RECHAZADOS.mkdir(exist_ok=True)

def validar_reglas_negocio(evento):
    errores = []

    temperatura = evento["temperature_c"]
    bateria = evento["battery_percent"]

    if not (2.0 <= temperatura <= 8.0):
        if temperatura < 2.0:
            errores.append("Temperatura menor a 2.0")
        else:
            errores.append("Temperatura mayor a 8.0")

    if bateria is not None and not (0 <= bateria <= 100):
        if bateria < 0:
            errores.append("Valor de batería inválido: menor que 0")
        else:
            errores.append("Valor de batería inválido: mayor que 100")

    return errores


eventos_por_fecha = defaultdict(list)
rechazados = []

recibidos = 0
rechazados_esquema = 0
rechazados_negocio = 0

with open("camara_frio.avsc", "r", encoding="utf-8") as archivo:
    esquema = json.load(archivo)

esquema = parse_schema(esquema)


with RUTA_ENTRADA.open("r", encoding="utf-8") as archivo:
    for numero_linea, linea in enumerate(archivo, start=1):
        recibidos += 1

        try:
            evento = json.loads(linea)
        except json.JSONDecodeError as error:
            print(error)
            continue

        try:
            validate(evento, esquema, raise_errors=True)
        except Exception as error:
            rechazados_esquema += 1
            rechazados.append(evento)
            continue

        errores = validar_reglas_negocio(evento)
        if errores:
            rechazados_negocio += 1
            rechazados.append(evento)
            continue

        # Si llega aquí, el evento es válido.
        # Falta obtener su fecha y añadirlo al grupo correcto.

        instante = datetime.fromisoformat(
            evento["timestamp"].replace("Z", "+00:00")
        )
        fecha = instante.date().isoformat()

        # TODO 8: añadir evento a eventos_por_fecha usando fecha como clave.

        eventos_por_fecha[fecha].append(evento)

for fecha, eventos_fecha in sorted(eventos_por_fecha.items()):
    carpeta_fecha = RUTA_RAW / f"fecha={fecha}"
    carpeta_fecha.mkdir(parents=True, exist_ok=True)

    nombre = f"camara_frio_{fecha}.avro"
    ruta_avro = carpeta_fecha / nombre

    with ruta_avro.open("wb") as archivo:
        # TODO 9: utilizar writer() con:
        # archivo, esquema, eventos_fecha y codec="deflate".
        writer(archivo, esquema, eventos_fecha, codec="deflate")

    print(fecha, "→", len(eventos_fecha), "eventos")


ruta_salida = RUTA_RECHAZADOS / "eventos_rechazados.ndjson"
with ruta_salida.open("w", encoding="utf-8") as archivo:
    for rechazo in rechazados:
        # TODO 10: convertir rechazo a JSON y añadir un salto de línea.
         archivo.write(json.dumps(rechazo, ensure_ascii=False) + "\n")

validos = sum(len(lista) for lista in eventos_por_fecha.values())

print("Registros recibidos:", recibidos)
print("Registros válidos:", validos)
print("Rechazados por esquema:", rechazados_esquema)
print("Rechazados por negocio:", rechazados_negocio)
print("Particiones RAW:", len(eventos_por_fecha))

archivos_avro = sorted(Path("RAW").glob("fecha=*/*.avro"))
total_recuperado = 0

for ruta_avro in archivos_avro:
    with ruta_avro.open("rb") as archivo:
        # TODO 11: leer y contar los eventos del archivo.
        cantidad = ...

    total_recuperado += cantidad
    print(ruta_avro, cantidad)

print("Total recuperado:", total_recuperado)