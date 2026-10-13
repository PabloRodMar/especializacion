menu = """ 1. Añadir un contacto: Guardar un nuevo registro (nombre y teléfono). 
2. Buscar un contacto: Consultar el teléfono de una persona o notificar si no existe.
3. Editar un contacto: Modificar el número de teléfono de un contacto guardado.
4. Eliminar un contacto: Borrar un registro de la agenda.
5. Mostrar todos los contactos: Imprimir la lista completa de contactos guardados. 
0. Salir\n"""

agenda = {}

print("Bienvenido a la agenda de contactos")

while True:
    opcion = input("\nEscoja una opción: ")
    while opcion != 0:
        match int(opcion):
            case 0:
                exit()
            case 1:
                nombre = input("Introduce el nombre del contacto: ")
                numero = input("Introduce su número de teléfono: ")
                agenda[nombre] = numero
                print("Número guardado correctamente")
            case 2:
                nombre = input("Introduce el nombre del contacto que quieras consultar: ")
                mensaje_no_encontrado = "No se ha encontrado el contacto."
                numero = agenda.get(nombre, mensaje_no_encontrado)
                if numero == mensaje_no_encontrado:
                    print(mensaje_no_encontrado)
                else:
                    print(f"Número de {nombre}: {numero}")
            case 3:
                nombre = input("Introduce el nombre del contacto cuyo número quieres editar: ")
                numero = input("Introduce el nuevo número de teléfono: ")
                agenda[nombre] = numero
                print("\nNúmero actualizado correctamente")
            case 4:
                nombre = input("Introduce el nombre del contacto que quieras eliminar: ")
                agenda.pop(nombre)
                print("Número eliminado correctamente")
            case 5:
                print()
                for nombre, numero in agenda.items():
                    print(f"Nombre: {nombre} número: {numero}")
        opcion = input("\nEscoja una opción: ")