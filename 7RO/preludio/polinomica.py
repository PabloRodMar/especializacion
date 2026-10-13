def entre_primos(n: int) -> list:
    lista_devolver = []
    contador = 2
    while n != 1:
        if n % contador == 0:
            lista_devolver.append(contador)
            n /= contador
            contador = 2
        else:
            print(f"Cargando... {int((contador / n) * 100)}%", end="\r", flush=True)
        contador += 1

    print(" " * 80, end="\r", flush=True)
    return lista_devolver

print(entre_primos(100003))