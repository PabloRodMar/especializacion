import time
import numpy as np
import sys

n = 100_000_000
lista = list(range(n))
arr = np.arange(n)

t = time.perf_counter()
cuadrados_lista = [x * x for x in lista]
t_lista = time.perf_counter() - t

t = time.perf_counter()
cuadrados_np = arr * arr
t_np = time.perf_counter() - t

print(f"\nLista: {t_lista:.4f} s | NumPy: {t_np:.4f} s")
print("Memoria de la lista: ", sys.getsizeof(cuadrados_lista))
print("\nMemoria del array:", arr.nbytes, "bytes")