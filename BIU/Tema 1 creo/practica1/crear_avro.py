import json
from pathlib import Path

from fastavro import parse_schema, writer, reader
from fastavro.validation import validate

# 1. Leer el contrato camara_frio.avsc
with open("camara_frio.avsc", "r", encoding="utf-8") as archivo:
    esquema = json.load(archivo)

# 2. Preparar y parsear el esquema utilizando parse_schema().
esquema = parse_schema(esquema)

# (para el paso 4)
lista_eventos = []

# 3. Leer camara_frio.ndjson línea por línea. 
# 4. Convertir cada línea JSON en un diccionario con json.loads(). 
# 5. Almacenar los eventos en una lista Python.
with open("camara_frio.ndjson", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        evento = json.loads(linea)
        lista_eventos.append(evento)

# 6. Imprimir en consola el número de eventos recibidos.
print(f"Total de eventos: {len(lista_eventos)}")


for evento in lista_eventos:
    validate(evento, esquema, raise_errors=True)

eventos_validos = []
for evento in lista_eventos:
    bateria = evento["battery_percent"]
    temperatura = evento["temperature_c"]
    if 2.0 <= temperatura <= 8.0 and (bateria is None or 0 <= bateria <= 100):
        eventos_validos.append(evento)
    else:
        print(f"Descartado: {evento}")
        if bateria <= 0:
            print("Motivo: Sin batería")
        elif bateria > 100:
            print("Motivo: Valor de batería inválido.")
        elif temperatura <= 2.0:
            print("Motivo: Temperatura menor a 2.0")
        elif temperatura >= 8.0:
            print("Motivo: Temperatura mayor a 8.0")

# 7. Crear el archivo binario camara_frio.avro.
# 8. Aplicar la compresión por bloques codec="deflate"
with open("camara_frio.avro", "wb") as archivo:
    writer(archivo, esquema, eventos_validos, codec="deflate")

# 9. Volver a abrir y leer el archivo camara_frio.avro en modo binario ("rb").
# 10. Mostrar en pantalla el esquema escritor incrustado y los 10 eventos recuperados.
with open("camara_frio.avro", "rb") as archivo:
    lector = reader(archivo)

    print("\nEsquema escritor incrustado:")
    print(json.dumps(lector.writer_schema))

    print("\nEventos recuperados:")
    eventos_recuperados = list(lector)
    for evento in eventos_recuperados:
        print(evento)

print("\nProceso finalizado")