import random
from dataclasses import dataclass, field

# =====================================================================
# DATOS DE PARTIDA (no modificar)
# =====================================================================

# id: (nombre, tipo, categoria, potencia, precision, pp)
MOVIMIENTOS = {
    1: ("Placaje", "normal", "fisico", 40, 100, 35),
    2: ("Golpe Cuerpo", "normal", "fisico", 85, 100, 15),
    3: ("Ataque Rápido", "normal", "fisico", 40, 100, 30),
    4: ("Ascuas", "fuego", "especial", 40, 100, 25),
    5: ("Lanzallamas", "fuego", "especial", 90, 100, 15),
    6: ("Pistola Agua", "agua", "especial", 40, 100, 25),
    7: ("Hidrobomba", "agua", "especial", 110, 80, 5),
    8: ("Látigo Cepa", "planta", "fisico", 45, 100, 25),
    9: ("Hoja Afilada", "planta", "fisico", 55, 95, 25),
    10: ("Impactrueno", "electrico", "especial", 40, 100, 30),
    11: ("Rayo", "electrico", "especial", 90, 100, 15),
    12: ("Excavar", "tierra", "fisico", 80, 100, 10),
    13: ("Terremoto", "tierra", "fisico", 100, 100, 10),
}

# nombre: (tipo, (hp, ataque, defensa, at_especial, def_especial, velocidad))
POKEDEX = {
    "Venusaur": ("planta", (80, 82, 83, 100, 100, 80)),
    "Charizard": ("fuego", (78, 84, 78, 109, 85, 100)),
    "Blastoise": ("agua", (79, 83, 100, 85, 105, 78)),
    "Pikachu": ("electrico", (35, 55, 40, 50, 50, 90)),
    "Sandslash": ("tierra", (75, 100, 110, 45, 55, 65)),
    "Snorlax": ("normal", (160, 110, 65, 65, 110, 30)),
}

# (tipo_ataque, tipo_defensor): multiplicador. Lo que no aparece vale 1.0
TABLA_TIPOS = {
    ("fuego", "planta"): 2.0, ("fuego", "agua"): 0.5, ("fuego", "fuego"): 0.5,
    ("agua", "fuego"): 2.0, ("agua", "tierra"): 2.0,
    ("agua", "agua"): 0.5, ("agua", "planta"): 0.5,
    ("planta", "agua"): 2.0, ("planta", "tierra"): 2.0,
    ("planta", "fuego"): 0.5, ("planta", "planta"): 0.5,
    ("electrico", "agua"): 2.0, ("electrico", "tierra"): 0.0,
    ("electrico", "planta"): 0.5, ("electrico", "electrico"): 0.5,
    ("tierra", "fuego"): 2.0, ("tierra", "electrico"): 2.0,
    ("tierra", "planta"): 0.5,
}

@dataclass
class Movimiento:
    id_mov: int
    nombre: str
    tipo: str
    categoria: str
    potencia: int
    presicion: int
    pp: int

    def tiene_pp(self) -> bool:
        if self.pp > 0:
            return True
        else:
            return False

    def gastar_pp(self) -> None:
        if self.pp > 0:
            self.pp -= 1

    def acierta(self) -> bool:
        return random.random() < (self.presicion / 100)

    def __str__(self):
        return f"Movimiento: {self.nombre} -- Tipo:{self.tipo} -- Pot: {self.potencia} -- Prec: {self.presicion} -- PP: {self.pp}"

def crear_movimiento(id_mov) -> Movimiento | None:
    if id_mov in MOVIMIENTOS.keys():
        return Movimiento(id_mov, MOVIMIENTOS[id_mov][0], MOVIMIENTOS[id_mov][1], MOVIMIENTOS[id_mov][2], MOVIMIENTOS[id_mov][3], MOVIMIENTOS[id_mov][4], MOVIMIENTOS[id_mov][5])
    else:
        print(f"⚠️   El movimiento con ID {id_mov} no es de esta generación.")
        return None

class Pokemon:
    MAX_MOVIMIENTOS = 4

    def __init__(self, nombre: str, nivel: int, ids_movimientos: list[int]):

        lista_movimientos = []
        for movimiento in ids_movimientos:
            lista_movimientos.append(crear_movimiento(movimiento))

        self.nombre = nombre
        self.tipo = POKEDEX[nombre][0]
        self.nivel = nivel
        self.hp_max = self.calcular_hp(POKEDEX[nombre][1][0], nivel)
        self.hp_actual = self.hp_max
        self.ataque = self.calcular_stat(POKEDEX[nombre][1][1], nivel)
        self.defensa = self.calcular_stat(POKEDEX[nombre][1][2], nivel)
        self.at_especial = self.calcular_stat(POKEDEX[nombre][1][3], nivel)
        self.def_especial = self.calcular_stat(POKEDEX[nombre][1][4], nivel)
        self.velocidad = self.calcular_stat(POKEDEX[nombre][1][5], nivel)
        self.movimientos = lista_movimientos

    @staticmethod
    def calcular_hp(base, nivel):
        return (2 * base * nivel) // 100 + nivel + 10

    @staticmethod
    def calcular_stat(base, nivel):
        return (2 * base * nivel) // 100 + 5

    def esta_debilitado(self):
        return self.hp_actual <= 0

    def recibir_danio(self, cantidad):
        self.hp_actual -= cantidad
        if self.hp_actual < 0:
            self.hp_actual = 0

    def movimientos_disponibles(self):
        mov_disp = []
        for movimiento in self.movimientos:
            if movimiento.tiene_pp():
                mov_disp.append(movimiento)

    def __str__(self):
        return f"Pokémon: {self.nombre} (LVL {self.nivel}) [{self.tipo}] HP: {self.hp_actual}/{self.hp_max}"

    def calcular_danio(self, objetivo: Pokemon, mov: Movimiento) -> tuple:
        categoria_ataque = "fisico"
        if mov.categoria == "especial":
            categoria_ataque = "especial"

        stab = 1.0
        if mov.tipo == self.tipo:
            stab = 1.5
        
        efectividad = TABLA_TIPOS.get((mov.tipo, objetivo.tipo), 1.0)

        varianza = random.randrange(85, 100) / 100

        if categoria_ataque == "fisico":
            base  = ((2 * self.nivel / 5 + 2) * mov.potencia *  objetivo.ataque / self.defensa) / 50 + 2
        else:
            base  = ((2 * self.nivel / 5 + 2) * mov.potencia *  objetivo.at_especial / self.def_especial) / 50 + 2

        dano = int(base * stab * efectividad * varianza)

        if dano < 1 and efectividad != 0:
            dano = 1

        return dano, efectividad

    def atacar(self, objetivo: Pokemon, mov: Movimiento) -> None:
        mov.gastar_pp()

        dano, eficacia = self.calcular_danio(objetivo, mov)

        print(f"¡{self.nombre} ha usado {mov.nombre}!")

        if mov.acierta():
            if eficacia == 2.0:
                print(f"¡Es muy eficaz!")
            elif eficacia == 0.5:
                print(f"No es muy eficaz...")
            elif eficacia == 0.0:
                print(f"No afecta al {objetivo.nombre} rival...")

            if eficacia != 0:
                objetivo.recibir_danio(dano)
                print(f"¡El {objetivo.nombre} rival ha recibido {dano} de daño! HP: {objetivo.hp_actual}/{objetivo.hp_max}\n")

        else:
            print(f"\n¡{objetivo.nombre} ha evitado el ataque!")

@dataclass
class Entrenador:
    MAX_EQUIPO = 6

    nombre: str
    es_humano: False
    equipo: list[Pokemon]
    pokemon_actual = 0

    def agregar_pokemon(self, pokemon: Pokemon) -> bool:
        if len(self.equipo) < 6:
            self.equipo.append(pokemon)
            return True
        else:
            print("¡El equipo está lleno! No se pueden añadir más pokémon")
            return False

    def pokemon_activo(self) -> Pokemon | None:
        return self.equipo[self.pokemon_actual]

    def tiene_pokemon_disponibles(self) -> bool:
        return self.equipo

    def mostrar_equipo(self):
        for pokemon in self.equipo:
            print(pokemon)
            if pokemon.esta_debilitado():
                print("Estado: Debilitado")
            else:
                print("Estado: Disponible")

    def elegir_movimiento(self) -> Movimiento | None:
        movimiento = self.equipo[self.pokemon_actual].movimientos[random.randrange(0, 3)]
        if movimiento.tiene_pp():
            return movimiento

    def pokemon_debilitado(self):
        if self.equipo[self.pokemon_actual].esta_debilitado():
            print(f"¡{self.equipo[self.pokemon_actual].nombre} se ha debilitado!")
            self.equipo.pop(self.pokemon_actual)
            if self.equipo:
                print(f"Cambiando a {self.equipo[self.pokemon_actual].nombre}\n")

class Batalla:
    def __init__(self, entrenador: Entrenador, rival: Entrenador, turno = 1):
        self.turno = turno
        self.entrenador = entrenador
        self.rival = rival

    def determinar_orden(self) -> list[Entrenador]:
        if self.entrenador.equipo[self.entrenador.pokemon_actual].velocidad > self.rival.equipo[self.rival.pokemon_actual].velocidad:
            return (self.entrenador, self.rival)
        else:
            return (self.rival, self.entrenador)

    def rival_de(rival: Entrenador):
        return rival.nombre

    def mostrar_estado(self):
        return f"Turno {self.turno}\n{self.entrenador}: {self.entrenador.equipo[self.entrenador.pokemon_actual]}\n{self.rival}: {self.rival.equipo[self.rival.pokemon_actual]}"

    def ejecutar_turno(self):
        self.mostrar_estado()

        mov_entrenador = self.entrenador.elegir_movimiento()
        mov_rival = self.rival.elegir_movimiento()

        primer_ataque, segundo_ataque = self.determinar_orden()

        if primer_ataque is self.entrenador:
            primer_mov = mov_entrenador
            segundo_mov = mov_rival
        else:
            primer_mov = mov_rival
            segundo_mov = mov_entrenador

        primer_ataque.equipo[primer_ataque.pokemon_actual].atacar(segundo_ataque.equipo[segundo_ataque.pokemon_actual], primer_mov)

        if segundo_ataque.equipo[primer_ataque.pokemon_actual].esta_debilitado():
            segundo_ataque.pokemon_debilitado()
            return

        segundo_ataque.equipo[segundo_ataque.pokemon_actual].atacar(primer_ataque.equipo[primer_ataque.pokemon_actual], segundo_mov)

        if primer_ataque.equipo[segundo_ataque.pokemon_actual].esta_debilitado():
            primer_ataque.pokemon_debilitado()

    def ganador(self):
        while self.entrenador.equipo and self.rival.equipo:
            return None
        if not self.rival.equipo:
            return self.entrenador
        else:
            return self.rival

    def iniciar(self):
        print("============== ¡INICIO DEL COMBATE! ==============")
        print(f"\n======= {self.entrenador.nombre} --- VS --- {self.rival.nombre} =======\n")

        print(f"============== {self.entrenador.equipo[self.entrenador.pokemon_actual].nombre} VS {self.rival.equipo[self.rival.pokemon_actual].nombre} ==============\n")

        while self.ganador() is None:
            print(f"============ TURNO {self.turno} ============")
            self.ejecutar_turno()
            self.turno += 1

        print("\n\n=================== FIN DEL COMBATE ===================\n")

        if self.ganador() == self.entrenador:
            print(f"¡El entrenador {self.rival.nombre} se ha quedado sin pokémons! ¡{self.entrenador.nombre} gana el combate!")
        else:
            print(f"¡El entrenador {self.entrenador.nombre} se ha quedado sin pokémons! ¡{self.rival.nombre} gana el combate!")

p1 = Pokemon("Venusaur", 50, [10, 11, 3, 1])
p2 = Pokemon("Pikachu", 50, [10, 11, 3, 2])

p3 = Pokemon("Charizard", 50, [10, 11, 3, 2])
p4 = Pokemon("Pikachu", 50, [10, 11, 3, 2])

e1 = Entrenador("Pablo", True, [p1, p2])
e2 = Entrenador("N", True, [p3, p4])

combate = Batalla(e1, e2)

combate.iniciar()