menu = """
1. Añadir un ítem
2. Buscar un ítem
3. Editar precio o stock
4. Eliminar un ítem
5. Mostrar todo el inventario
"""

alforja = {}

print("Bienvenido a la alforja")

while True:
    print(menu)
    opcion = input("Selecciona una opción (1-5): ")
    while opcion != 0:
        match int(opcion):
            case 0:
                exit()
            case 1:
                nombre = input("Introduce el nombre del ítem: ")
                precio = float(input("Introduce el precio del ítem: "))
                stock = int(input("Introduce el stock del ítem: "))
                alforja[nombre] = [precio, stock]
                print("Ítem guardado correctamente")
            case 2:
                nombre = input("Introduce el nombre del ítem que quieras consultar: ")
                if nombre in alforja:
                    stock = alforja[nombre][1]
                    if stock > 0:
                        print("Producto disponible.")
                    else:
                        print("Producto agotado")
                else:
                    print("Producto no encontrado. ")
            case 3:
                nombre = input("Introduce el nombre del ítem a modificar: ")
                if nombre in alforja:
                    nuevo_precio = input("Introduzca el nuevo precio del producto (pulse enter para no modificar): ")
                    nuevo_stock = input("Introduzca el nuevo precio del producto (pulse enter para no modificar): ")
                    if not nuevo_stock and not nuevo_precio:
                        print("Sin cambios, pulsaste esto para nada.")
                    elif not nuevo_precio:
                        alforja[nombre][0] = float(precio)
                        print("Se ha cambiado el precio del ítem correctamente.")
                    elif not nuevo_stock:
                        alforja[nombre][1] = int(stock)
                        print("Se ha cambiado el stock del ítem correctamente.")      
                    else:
                        alforja[nombre] = float(precio), int(stock)
                        print("Se han actualizado el precio y el stock del ítem correctamente.")
                else:
                    print("Producto no encontrado")
            case 4:
                nombre = input("Introduce el nombre del ítem a eliminar: ")
                if nombre in alforja:
                    alforja.pop(nombre)
                    print("Ítem eliminado correctamente.")
                else:
                    print("Ítem no encontrado")
            case 5:
                if not alforja:
                    print("¡La alforja no tiene ítems!")
                else:
                    for nombre, (precio, stock) in alforja.items():
                        print(f"Nombre del ítem: {nombre} -- Precio: {precio} -- Stock: {stock}")
        print(menu)
        opcion = input("\nEscoja una opción: ")