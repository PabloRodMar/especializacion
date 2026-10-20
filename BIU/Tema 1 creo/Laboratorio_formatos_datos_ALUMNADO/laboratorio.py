#!/usr/bin/env python3
"""
Experimentos reproducibles del laboratorio de formatos de datos.

Uso:
    python3 laboratorio.py todo
    python3 laboratorio.py tamanos
    python3 laboratorio.py proyeccion
    python3 laboratorio.py particiones
    python3 laboratorio.py esquema
    python3 laboratorio.py csv_roto
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import statistics
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "datos"


def human_size(n):
    units = ["B", "KiB", "MiB", "GiB"]
    value = float(n)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:,.1f} {unit}"
        value /= 1024


def timed(label, fn):
    start = time.perf_counter()
    result = fn()
    elapsed = (time.perf_counter() - start) * 1000
    return {"estrategia": label, "resultado": result, "tiempo_ms": round(elapsed, 2)}


def tamanos():
    print("\nEXPERIMENTO 1. TAMAÑO Y COMPRESIÓN")
    files = [
        DATA / "telemetria.csv",
        DATA / "telemetria.csv.gz",
        DATA / "telemetria.ndjson",
        DATA / "telemetria.ndjson.gz",
    ]
    parquet = DATA / "telemetria_snappy.parquet"
    if parquet.exists():
        files.append(parquet)
    base = files[0].stat().st_size
    results = []
    for path in files:
        size = path.stat().st_size
        ratio = base / size
        results.append((path.name, size, ratio))
        print(f"{path.name:30} {human_size(size):>12}  CSV/tamaño={ratio:5.2f}x")
    columns = sum(p.stat().st_size for p in (DATA / "columnas_comprimidas").glob("*.gz"))
    print(f"{'columnas_comprimidas (total)':30} {human_size(columns):>12}  CSV/tamaño={base/columns:5.2f}x")
    return results


def _csv_average():
    values = []
    with (DATA / "telemetria.csv").open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if row["event_date"] == "2026-09-08":
                values.append(float(row["engine_temp_c"]))
    return round(statistics.fmean(values), 4), len(values)


def _ndjson_average():
    values = []
    with (DATA / "telemetria.ndjson").open(encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            if row["event_date"] == "2026-09-08":
                values.append(float(row["engine_temp_c"]))
    return round(statistics.fmean(values), 4), len(values)


def _column_average():
    values = []
    folder = DATA / "columnas_comprimidas"
    with gzip.open(folder / "event_date.txt.gz", "rt", encoding="utf-8") as dates, gzip.open(
        folder / "engine_temp_c.txt.gz", "rt", encoding="utf-8"
    ) as temps:
        for day, temp in zip(dates, temps):
            if day.rstrip("\n") == "2026-09-08":
                values.append(float(temp))
    return round(statistics.fmean(values), 4), len(values)


def proyeccion():
    print("\nEXPERIMENTO 2. PROYECCIÓN DE COLUMNAS")
    results = [
        timed("CSV: todas las columnas", _csv_average),
        timed("NDJSON: objetos completos", _ndjson_average),
        timed("Columnar simulado: fecha + temperatura", _column_average),
    ]
    full_bytes = (DATA / "telemetria.csv").stat().st_size
    projected_bytes = sum((DATA / "columnas_comprimidas" / name).stat().st_size for name in ["event_date.txt.gz", "engine_temp_c.txt.gz"])
    for item in results:
        print(f"{item['estrategia']:42} resultado={item['resultado']}  {item['tiempo_ms']:8.2f} ms")
    print(f"Bytes físicos de referencia: CSV={human_size(full_bytes)}, dos columnas comprimidas={human_size(projected_bytes)}")
    print("Nota: los tiempos locales varían. La evidencia principal es la cantidad de datos que cada diseño obliga a leer.")
    return results


def _scan_all_partitions(day, delegation):
    files = list((DATA / "particionado").glob("event_date=*/delegacion=*/part-000.csv.gz"))
    return _scan_files(files, day, delegation), files


def _scan_pruned_partitions(day, delegation):
    folder = DATA / "particionado" / f"event_date={day}" / f"delegacion={delegation}"
    files = list(folder.glob("part-*.csv.gz"))
    return _scan_files(files, day, delegation), files


def _scan_files(files, day, delegation):
    values = []
    for path in files:
        with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row["event_date"] == day and row["delegacion"] == delegation:
                    values.append(float(row["engine_temp_c"]))
    return round(statistics.fmean(values), 4), len(values)


def particiones():
    print("\nEXPERIMENTO 3. PARTITION PRUNING")
    day, delegation = "2026-09-08", "Sevilla"
    start = time.perf_counter()
    all_result, all_files = _scan_all_partitions(day, delegation)
    all_ms = (time.perf_counter() - start) * 1000
    start = time.perf_counter()
    pruned_result, pruned_files = _scan_pruned_partitions(day, delegation)
    pruned_ms = (time.perf_counter() - start) * 1000
    all_bytes = sum(p.stat().st_size for p in all_files)
    pruned_bytes = sum(p.stat().st_size for p in pruned_files)
    print(f"Escaneo total: {len(all_files)} archivos, {human_size(all_bytes)}, {all_ms:.2f} ms, resultado={all_result}")
    print(f"Con poda:      {len(pruned_files)} archivos, {human_size(pruned_bytes)}, {pruned_ms:.2f} ms, resultado={pruned_result}")
    print(f"Reducción de bytes candidatos: {all_bytes / pruned_bytes:.1f}x")
    return {"total": [len(all_files), all_bytes, all_result], "poda": [len(pruned_files), pruned_bytes, pruned_result]}


def _validate_type(value, allowed):
    mapping = {"integer": int, "number": (int, float), "string": str, "null": type(None)}
    for item_type in allowed:
        if item_type == "timestamp":
            if isinstance(value, str):
                try:
                    datetime_value = value.replace("Z", "+00:00")
                    from datetime import datetime

                    datetime.fromisoformat(datetime_value)
                    return True
                except ValueError:
                    continue
        elif isinstance(value, mapping[item_type]) and not (
            item_type in {"integer", "number"} and isinstance(value, bool)
        ):
            return True
    return False


def esquema():
    print("\nEXPERIMENTO 4. EVOLUCIÓN DE ESQUEMA")
    folder = DATA / "evolucion_esquema"
    contract = json.loads((folder / "contrato_esquema.json").read_text(encoding="utf-8"))
    for path in sorted(folder.glob("telemetria_*.ndjson")):
        errors = []
        with path.open(encoding="utf-8") as f:
            for line_number, line in enumerate(f, 1):
                row = json.loads(line)
                for field, rule in contract["fields"].items():
                    if field not in row:
                        if rule.get("required"):
                            errors.append((line_number, field, "ausente"))
                        continue
                    allowed = rule["type"] if isinstance(rule["type"], list) else [rule["type"]]
                    if not _validate_type(row[field], allowed):
                        errors.append((line_number, field, f"tipo {type(row[field]).__name__}"))
        status = "COMPATIBLE" if not errors else f"INCOMPATIBLE ({len(errors)} errores)"
        print(f"{path.name:38} {status}")
        for error in errors[:3]:
            print(f"  línea={error[0]}, campo={error[1]}, problema={error[2]}")


def csv_roto():
    print("\nEXPERIMENTO 5. CSV CORRUPTO")
    path = DATA / "telemetria_corrupta.csv"
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    expected = len(rows[0])
    broken = [(i, len(row)) for i, row in enumerate(rows[1:], 2) if len(row) != expected]
    print(f"Columnas esperadas: {expected}. Filas con cardinalidad distinta: {broken}")
    print("Diagnóstico esperado: una coma dentro de un texto no fue entrecomillada.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("experimento", choices=["todo", "tamanos", "proyeccion", "particiones", "esquema", "csv_roto"], nargs="?", default="todo")
    args = parser.parse_args()
    if not DATA.exists():
        raise SystemExit("Falta la carpeta datos. Ejecuta primero: python3 generar_datos.py")
    actions = {
        "tamanos": tamanos,
        "proyeccion": proyeccion,
        "particiones": particiones,
        "esquema": esquema,
        "csv_roto": csv_roto,
    }
    if args.experimento == "todo":
        for action in actions.values():
            action()
    else:
        actions[args.experimento]()


if __name__ == "__main__":
    main()
