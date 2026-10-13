from dataclasses import dataclass, field
from typing import List

@dataclass
class Producto:
    id_producto: int
    nombre: str
    precio: float
    stock: int = 0

    def calcular_valor_total(self) -> float:
        return self.precio * self.stock

    def mostrar_info(self) -> None:
        print(f"ID: {self.id_producto} -- Nombre del producto: {self.nombre} --- Precio: {self.precio}€ --- Stock disponible: {self.stock}")

@dataclass
class GestorInventario:

    productos: List[Producto] = field(default_factory=list)

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def listar_productos(self) -> None:
        print(f"{self.productos}")

    def buscar(self, id_recibida: int) -> Producto:
        for producto in self.productos:
            if producto.id_producto == id_recibida:
                return producto
            

print("¡¡¡¡¡¡¡¡¡¡¡ HOLAAAAAAAAAAAAA !!!!!!!!!!!!!!!\n")

print("""1: Agregar nuevo producto.
2: Listar todos los productos.
3: Buscar producto por ID.
4: Calcular valor total del inventario.
5: Salir.\n""")

opcion = int(input("Elije una opción: "))

gestor = GestorInventario()

while opcion != 0:
    match opcion:
        case 1:
            id = int(input("Inserte la id del producto: "))
            nombre = input("Inserte el nombre del producto: ")
            precio = float(input("Introduzca el precio del producto: "))
            stock = int(input("Introduzca el stock del producto: "))

            producto = Producto(id, nombre, precio, stock)
            gestor.agregar_producto(producto)

        case 2:
            gestor.listar_productos()

        case 3:
            id_buscada = int(input("\nIntroduce el id a buscar: "))
            gestor.buscar(id_buscada).mostrar_info()

        case 4:
            

    opcion = int(input("\nElije una opción: "))