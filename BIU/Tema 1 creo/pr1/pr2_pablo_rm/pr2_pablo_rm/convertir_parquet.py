from pathlib import Path
from datetime import datetime
from fastavro import reader
import pyarrow as pa
import pyarrow.parquet as pq

RUTA_RAW = Path("RAW")
RUTA_CURATED = Path("CURATED")
RUTA_CURATED.mkdir(exist_ok=True)

archivos_avro = sorted(RUTA_RAW.glob("fecha=*/*.avro"))

for ruta_avro in archivos_avro:
    fecha = ruta_avro.parent.name.split("=", 1)[1]

    with ruta_avro.open("rb") as archivo:
        eventos = list(reader(archivo))

    for evento in eventos:
        evento["timestamp"] = datetime.fromisoformat(
            evento["timestamp"].replace("Z", "+00:00")
        )

    carpeta_fecha = RUTA_CURATED / f"fecha={fecha}"
    carpeta_fecha.mkdir(parents=True, exist_ok=True)
    ruta_parquet = carpeta_fecha / f"camara_frio_{fecha}.parquet"

    tabla = pa.Table.from_pylist(eventos)

    # TODO 12: escribir tabla en ruta_parquet usando
    # pq.write_table() y compression="snappy".
    pq.write_table(tabla, ruta_parquet, compression="snappy")

    print(fecha, "→", len(eventos), "eventos convertidos")