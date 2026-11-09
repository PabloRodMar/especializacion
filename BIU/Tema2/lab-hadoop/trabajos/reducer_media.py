import sys

# Con --parcial actúa como combiner: devuelve suma y contador, nunca la media.
parcial = "--parcial" in sys.argv
actual, suma, n = None, 0.0, 0

def emitir(clave, suma, n):
    if parcial:
        print(f"{clave}\t{suma}\t{n}")
    else:
        print(f"{clave}\t{suma / n:.2f}\t{n}")

for linea in sys.stdin:
    clave, s, c = linea.rstrip("\n").split("\t")
    if actual is not None and clave != actual:
        emitir(actual, suma, n)
        suma, n = 0.0, 0
    actual = clave
    suma += float(s)
    n += int(c)

if actual is not None:
    emitir(actual, suma, n)
