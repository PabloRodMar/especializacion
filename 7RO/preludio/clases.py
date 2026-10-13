from dataclasses import dataclass, field
from typing import List

class Persona:

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentar(self) -> None:
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años.")

p1 = Persona("Arturo", 23)

p1.presentar()

@dataclass
class Estudiante:
    nombre: str
    edad: int
    nota: float = 0.0
    role: List[str] = field(default_factory=list)

e1 = Estudiante("Arturo", 25, 4.9)

print(e1)