import csv
import sys

# Emite: ciudad \t suma \t contador   (solo eventos en ruta)
for fila in csv.reader(sys.stdin):
    if not fila or fila[0] == "id_evento":      # cabecera o línea vacía
        continue
    try:
        ciudad, velocidad, estado = fila[3], float(fila[4]), fila[6]
    except (IndexError, ValueError):
        continue                                   # registro mal formado
    if estado == "ruta":
        print(f"{ciudad}\t{velocidad}\t1")
