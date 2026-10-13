frutas = ["Manzanas", "Platano", "Cereza"]

for fruta in frutas:
    print(fruta)

contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(f"{contador} es un numero impar")