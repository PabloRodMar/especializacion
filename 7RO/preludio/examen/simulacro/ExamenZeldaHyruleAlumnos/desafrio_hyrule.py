from dataclasses import dataclass
import random

CATALOGO_ARMAS = {
    101: {"nombre": "Espada de Viajero", "elemento": "fisico", "ataque": 16, "durabilidad": 20},
    102: {"nombre": "Mandoble Real", "elemento": "fisico", "ataque": 38, "durabilidad": 36},
    103: {"nombre": "Espada de Fuego", "elemento": "fuego", "ataque": 24, "durabilidad": 28},
    104: {"nombre": "Lanza de Hielo", "elemento": "hielo", "ataque": 20, "durabilidad": 32},
    105: {"nombre": "Cimitarra de Rayo", "elemento": "electrico", "ataque": 26, "durabilidad": 25},
    106: {"nombre": "Espada Maestra Ancestral", "elemento": "sagrado", "ataque": 60, "durabilidad": 50},
}

TABLA_ELEMENTAL = {
    ("fuego", "hielo"): 2.0,
    ("hielo", "fuego"): 2.0,
    ("electrico", "fisico"): 1.5,
    ("sagrado", "abismo"): 2.5,
    ("fuego", "fuego"): 0.5,
    ("hielo", "hielo"): 0.5,
    ("electrico", "electrico"): 0.5,
}

BESTIARIO_HYRULE = {
    "Bokoblin Carmesí": {"vida": 72, "ataque": 12, "defensa": 5, "elemento": "fisico"},
    "Lizalfos Ígneo": {"vida": 120, "ataque": 22, "defensa": 8, "elemento": "fuego"},
    "Lizalfos Gélido": {"vida": 120, "ataque": 22, "defensa": 8, "elemento": "hielo"},
    "Centaleón Plateado": {"vida": 240, "ataque": 45, "defensa": 18, "elemento": "abismo"},
}

@dataclass
class Arma:
    id_arma: int
    nombre: str
    elemento: str
    ataque_base: int
    durabilidad_max: int
    durabilidad_actual: int

    def esta_rota(self) -> bool:
        if self.durabilidad_actual <= 0:
            return True

    def desgastar(self, puntos: int = 1) -> bool:
        if self.durabilidad_actual - puntos <= 0:
            self.durabilidad_actual = 0
            return True
        self.durabilidad_actual -= puntos
        return False

    def __str__(self):
        return f"{self.nombre} -- Elemento {self.elemento} -- ATK: {self.ataque_base} -- Durabilidad: {self.durabilidad_actual}/{self.durabilidad_max}"

new_arma = Arma(1, "Espada", "fuego", 100, 10, 5)

print(new_arma)