"""Genera eventos sintéticos de vehículos (CSV) de forma reproducible.
Uso: python3 gen_eventos.py --filas 1000000 --fecha 2026-10-01 --semilla 42 [--sesgo 0.6] > eventos.csv
"""
import argparse, csv, random, sys
from datetime import datetime, timedelta

p = argparse.ArgumentParser()
p.add_argument("--filas", type=int, default=100_000)
p.add_argument("--fecha", default="2026-10-01")
p.add_argument("--semilla", type=int, default=42)
p.add_argument("--vehiculos", type=int, default=12_000)
p.add_argument("--sesgo", type=float, default=0.0,
               help="fracción de eventos que se asignan al vehículo V00001 (0 = sin sesgo)")
a = p.parse_args()

rnd = random.Random(a.semilla)
inicio = datetime.fromisoformat(a.fecha)
estados = ["ruta", "parado", "carga", "taller"]
pesos = [0.70, 0.20, 0.08, 0.02]
ciudades = ["Santa Cruz", "La Laguna", "La Orotava", "Puerto de la Cruz", "Icod"]

w = csv.writer(sys.stdout, lineterminator="\n")
w.writerow(["id_evento", "vehiculo", "ts", "ciudad", "velocidad", "bateria", "estado"])
for i in range(a.filas):
    if a.sesgo and rnd.random() < a.sesgo:
        v = 1
    else:
        v = rnd.randint(1, a.vehiculos)
    ts = inicio + timedelta(seconds=rnd.randint(0, 86_399))
    estado = rnd.choices(estados, pesos)[0]
    vel = round(rnd.uniform(5, 90), 1) if estado == "ruta" else 0.0
    w.writerow([f"E{i:09d}", f"V{v:05d}", ts.isoformat(), rnd.choice(ciudades),
                vel, rnd.randint(3, 100), estado])
