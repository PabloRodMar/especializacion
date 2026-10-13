bestiario = {
    "bokoblin": ("Monstruo Base", 50, 12, 15),
    "moblin": ("Monstruo Pesado", 120, 25, 40),
    "lizalfos": ("Monstruo Ágil", 85, 18, 30),
    "lynel": ("Bestia Legendaria", 450, 75, 250),
    "guardian": ("Artefacto Sheikah", 300, 55, 150)
}

i = 0
for bestia, caracteristicas in bestiario.items():
    i += 1
    print(f"Bestia nº {i}: {bestia} -- Tipo de monstruo: {caracteristicas[0]}")