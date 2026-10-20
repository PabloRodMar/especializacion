bestiario = {
    "bokoblin": ("Monstruo Base", 50, 12, 15),
    "moblin": ("Monstruo Pesado", 120, 25, 40),
    "lizalfos": ("Monstruo Ágil", 85, 18, 30),
    "lynel": ("Bestia Legendaria", 450, 75, 250),
    "guardian": ("Artefacto Sheikah", 300, 55, 150)
}

print("----- BESTIARIO -----\n")

i = 0
for bestia, caracteristicas in bestiario.items():
    i += 1
    print(f"Bestia nº {i}: {bestia.upper()} -- Tipo de monstruo: {caracteristicas[0]} -- Puntos de vida: {caracteristicas[1]} -- Ataque: {caracteristicas[2]} -- Recompensa: {caracteristicas[3]} rupias.")

enemigo = input("\nIntroduce el nombre del enemigo a combatir: ").lower().strip()

while enemigo not in bestiario.keys():
    print(f"\nNo se ha encontrado el enemigo :(")
    enemigo = input("\nIntroduce el nombre del enemigo a combatir: ").lower().strip()

print(f"\n{enemigo.upper()} -- Tipo de monstruo: {bestiario[enemigo][0]} -- Puntos de vida: {bestiario[enemigo][1]} -- Ataque: {bestiario[enemigo][2]} -- Recompensa: {bestiario[enemigo][3]} rupias.")

n_rondas = int(input(f"¿Cuántas rondas vas a combatir a el {enemigo}?: "))

atk_link = int(input("¿Cúanto ataque tiene tu espada?: "))

vida_actual = bestiario[enemigo][1]

cont_dano = 0

for ronda in range(1, n_rondas + 1):
    print(f"Ronda {ronda}:\n\n¡LINK ATACA! ---> Daño inflingido: {atk_link}")
    vida_actual -= atk_link
    print(f"Vida restante del {enemigo}: {vida_actual}")

    if vida_actual > 0:
        print(f"\n¡{enemigo} ATACA! --> Daño inflingido: {bestiario[enemigo][2]}")
        cont_dano += bestiario[enemigo][2]
        print(f"\nDaño total recibido por Link ---> {cont_dano}\n\n")
    else:
        print("\n¡¡¡¡¡¡¡¡¡ VICTORIA !!!!!!!!!!!!")
        print("\n----- Stats -----")
        print(f"\nDaño total recibido: {cont_dano}")
        print("Recogiendo rupias: \n")

        cont_rupias = 0
        total_rupias = bestiario[enemigo][3]

        while cont_rupias < total_rupias:
            cont_rupias += 5
            print(f"¡CHIKLIN! Rupias obtenidas: ({cont_rupias}/{total_rupias})")
        print()
        break