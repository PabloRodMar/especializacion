from dataclasses import dataclass
import random, math

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
    "Bokoblin Carmesi": {"vida": 72, "ataque": 12, "defensa": 5, "elemento": "fisico"},
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
        return f"{self.nombre} -- Elemento {self.elemento} -- ATK: {self.ataque_base} -- Durabilidad: {self.durabilidad_actual}/{self.durabilidad_max} ({"█" * self.durabilidad_actual}{"░" * (self.durabilidad_max - self.durabilidad_actual)})"

def fabricar_arma(id_arma: int) -> Arma | None:
    if id_arma in CATALOGO_ARMAS.keys():
        return Arma(id_arma, CATALOGO_ARMAS[id_arma]["nombre"], CATALOGO_ARMAS[id_arma]["elemento"], CATALOGO_ARMAS[id_arma]["ataque"], CATALOGO_ARMAS[id_arma]["durabilidad"], CATALOGO_ARMAS[id_arma]["durabilidad"])
    print(f"⚠️ El arma con ID {id_arma} no existe en la forja ancestral.")

class Guerrero:

    def __init__(self, nombre: str, vida_max: int, defensa_base: int, elemento_afin: str = "fisico"):
        self.nombre = nombre
        self.vida_max = vida_max
        self.vida_actual = vida_max
        self.defensa_base = defensa_base
        self.elemento_afin = elemento_afin

    def esta_vivo(self) -> bool:
        if self.vida_actual > 0:
            return True
        else:
            return False

    def recibir_danio(self, cantidad: int) -> int:
        danio_real = max(1, cantidad - (self.defensa_base // 3))
        if self.vida_actual - danio_real < 0:
            self.vida_actual = 0
        else:
            self.vida_actual -= danio_real
        return danio_real

    def curar(self, cantidad: int) -> int:
        if self.vida_actual + cantidad > self.vida_max:
            self.vida_actual = self.vida_max
        else:
            self.vida_actual += cantidad

    def barra_vida(self) -> str:
        return "❤️ " * (math.ceil(self.vida_actual / 20)) + "🖤" * (math.ceil((self.vida_max - self.vida_actual) / 20))

    def __str__(self) -> str:
        return f"{self.nombre} [{self.elemento_afin.upper()}] | {self.barra_vida()}  ({self.vida_actual}/{self.vida_max}) | Def: {self.defensa_base}" 

def calcular_danio_combate(arma: Arma, defensor: Guerrero) -> tuple[int, float, bool]:
    multiplicador = 1.0
    if (arma.elemento, defensor.elemento_afin) in TABLA_ELEMENTAL:
        multiplicador = TABLA_ELEMENTAL[arma.elemento, defensor.elemento_afin]

    es_critico = False
    critico = 1.0
    if random.random() < 0.15:
        critico = 1.5
        es_critico = True

    varianza = random.uniform(0.90, 1.10)

    danio_bruto = arma.ataque_base * multiplicador * critico * varianza

    return max(1, int(danio_bruto)), multiplicador, es_critico

class Alforja:
    CAPACIDAD_MAX = 5

    def __init__(self):
        self.armas: list[Arma] = []
        self.indice_equipada: int = 0

    def guardar_arma(self, arma: Arma) -> bool:
        if len(self.armas) >= self.CAPACIDAD_MAX:
            print("¡La alforja esta llena! El arma no cabe")
            return False
        else:
            self.armas.append(arma)
            return True

    def arma_equipada(self) -> Arma | None:
        return self.armas[self.indice_equipada]

    def cambiar_arma(self, indice: int) -> bool:
        if (0 <= indice < len(self.armas)):
            self.indice_equipada = indice
            self.arma_equipada()
            print(f"Se ha cambiado al siguiente arma: {self.armas[self.indice_equipada].nombre}")
            if self.arma_equipada().esta_rota():
                self.retirar_rota()
            return True
        else:
            print("Error: No existe un arma en ese hueco de inventario")
            return False

    def retirar_rota(self) -> Arma | None:
        self.armas.pop(self.indice_equipada)
        print("EL ARMA ESTA ROTAAA (no de que esté OP, si no que se rompió)")
        self.cambiar_arma(self.indice_equipada - 1)

    def mostrar_alforja(self) -> None:
        for arma in self.armas:
            print(f"{arma}")

class CombateHyrule:

    def __init__(self, heroe: Guerrero, alforja: Alforja, monstruo: Guerrero):
        self.turno = 1
        self.heroe = heroe
        self.alforja = alforja
        self.monstruo = monstruo

    def ejecutar_ataque_heroe(self) -> None:
        if self.alforja:
            dano_a_monstruo = calcular_danio_combate(self.alforja.arma_equipada(), self.monstruo)[0]
        else:
            dano_a_monstruo = calcular_danio_combate(4, self.monstruo)[0]

        danio_recibido = self.monstruo.recibir_danio(dano_a_monstruo)

        print(f"¡{self.heroe.nombre} ha atacado a {self.monstruo.nombre} y ha recibido {danio_recibido} puntos de daño! {self.monstruo.barra_vida()} -- ({self.monstruo.vida_actual}/{self.monstruo.vida_max})\n")

        self.alforja.armas[self.alforja.indice_equipada].desgastar()

        if self.alforja.armas[self.alforja.indice_equipada].durabilidad_actual == 0:
            self.alforja.retirar_rota()

    def turno_monstruo(self) -> None:
        ataque = random.randrange(BESTIARIO_HYRULE[self.monstruo.nombre]["ataque"] - 4, BESTIARIO_HYRULE[self.monstruo.nombre]["ataque"] + 6)
        self.heroe.recibir_danio(ataque)
        print(f"¡{self.monstruo.nombre} contraataca! ¡{self.heroe.nombre} ha recibido {ataque} puntos de daño! {self.heroe.barra_vida()} -- ({self.heroe.vida_actual}/{self.heroe.vida_max})\n")

    def iniciar(self) -> str:
        while self.heroe.esta_vivo() and self.monstruo.esta_vivo():
            if self.monstruo.vida_actual == self.monstruo.vida_max and self.heroe.vida_max == self.heroe.vida_actual:
                print(" ================= ¡COMIENZA EL COMBATE! =================")
                print(f"{self.heroe.nombre} {self.heroe.barra_vida()} ({self.heroe.vida_actual}/{self.heroe.vida_max}) ----- VS ----- {self.monstruo.nombre} {self.monstruo.barra_vida()} ({self.monstruo.vida_actual}/{self.monstruo.vida_max})\n")
            print(f" ===================== ¡TURNO {self.turno}! =====================")
            self.ejecutar_ataque_heroe()
            self.turno_monstruo()
            self.turno += 1
        if not self.monstruo.esta_vivo():
            return "¡Victoria!"
        else:
            return "¡Derrota!"

bokoblin = Guerrero("Bokoblin Carmesi", 72, 5)
link = Guerrero("Link", 100, 5)
alforja = Alforja()
arma = fabricar_arma(105)

alforja.guardar_arma(arma)

sim = CombateHyrule(link, alforja, bokoblin)

print(sim.iniciar())